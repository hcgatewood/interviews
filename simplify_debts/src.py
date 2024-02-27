"""
Given a list of loan transactions, return the minimum-length list of repayment transactions to settle all debts.
"""

from collections import deque
from copy import deepcopy
from dataclasses import dataclass
from typing import Generic, Iterable, TypeVar

import matplotlib.pyplot as plt
import networkx as nx
from typs import Edge, Edges, FlowWeight, Loan, Parents, Repayment, Weight

from lib import defaultdict

DEBUG = False
PLOT = False


def simplify_debts(loans: list[Loan]) -> list[Repayment]:
    return WeightedDAG.from_loans(loans).simplified().to_repayments()


class DAG(defaultdict[str, Edges[Weight]], Generic[Weight]):
    def __str__(self):
        edges = [f"{e}" for e in self.edges()]
        return "\n".join(edges)

    def vertices(self) -> Iterable[str]:
        return set(self.keys()) | set(b for bs in self.values() for b in bs)

    def edges(self) -> Iterable[Edge]:
        return (Edge(a, b, weight) for a, bs in self.items() for b, weight in bs.items())

    def plot(self, msg: str = "") -> None:
        if not PLOT:
            return
        g = nx.DiGraph()
        g.add_weighted_edges_from((e for e in self.edges() if e))
        pos = nx.planar_layout(g)
        nx.draw(g, pos, with_labels=True, node_color="r", font_color="w")
        _ = nx.draw_networkx_edge_labels(g, pos, edge_labels=nx.get_edge_attributes(g, "weight"))
        plt.text(0.1, 0.9, msg, fontsize=16, transform=plt.gca().transAxes)
        plt.show()


class WeightedDAG(DAG[float]):
    T = TypeVar("T", bound="WeightedDAG")

    def __init__(self, *args, **kwargs):
        super().__init__(Edges(float), *args, **kwargs)

    @classmethod
    def from_loans(cls: T, loans: list[Loan]) -> T:
        dag = cls()
        dag.build(loans)
        dag.plot("initial")
        return dag

    def build(self, loans: list[Loan]) -> None:
        for loan in loans:
            for debtor, amount in loan.debtors.items():
                self.update_edge(debtor, loan.creditor, amount)
        self.normalize()

    def update_edge(self, a: str, b: str, weight: float) -> None:
        s, t = min(a, b), max(a, b)
        weight = weight if s == a else -weight
        self[s][t] += weight

    def normalize(self) -> None:
        normalized = defaultdict(lambda: defaultdict(float))
        for a, b, amount in self.edges():
            if amount > 0:
                normalized[a][b] = amount
            if amount < 0:
                normalized[b][a] = -amount
        self.clear()
        self.update(normalized)

    def simplified(self) -> "WeightedDAG":
        flowdag = FlowDAG.from_dag(self)
        unvisited = sorted(set(self.edges()) | {Edge(v, v, 0) for v in self.vertices()})
        while unvisited:
            a, b, _ = unvisited.pop()
            debug(f"checking {a} -> {b}")
            flowdag.to_dag().plot(f"before: {a} to {b}")
            before = deepcopy(set(flowdag.edges()))
            maxflow = MaxFlow(flowdag, a, b).run()
            debug(f"{a} -> {b} had maxflow {maxflow}", indent=1)
            if maxflow:
                flowdag = flowdag.pruned()
                if a != b:
                    flowdag[a][b] = FlowWeight(0, maxflow)
                    flowdag[b][a] = FlowWeight(0, 0)
                after = deepcopy(set(flowdag.edges()))
                debug(f"removed: {sorted(before - after)}", indent=1)
                debug(f"added: {sorted(after - before)}", indent=1)
        dag = flowdag.to_dag()
        dag.plot("final")
        return dag

    def to_repayments(self) -> list[Repayment]:
        repayments = sorted([Repayment(a, bs) for a, bs in self.items()])
        return repayments


class FlowDAG(DAG[FlowWeight]):
    T = TypeVar("T", bound="FlowDAG")

    def __init__(self, *args, **kwargs):
        super().__init__(Edges(FlowWeight), *args, **kwargs)

    @classmethod
    def from_dag(cls: T, dag: WeightedDAG) -> T:
        flowdag = cls()
        flowdag.build(dag)
        return flowdag

    def build(self, dag: DAG) -> None:
        for a, b, weight in dag.edges():
            self[a][b] = FlowWeight(0, weight)
            self[b][a] = FlowWeight(0, 0)

    def pruned(self) -> "FlowDAG":
        pruned = FlowDAG()
        for a, b, flow in self.edges():
            if flow.capacity > 0 and flow.free > 0:
                pruned[a][b] = FlowWeight(0, flow.free)
                pruned[b][a] = FlowWeight(0, 0)
        return pruned

    def to_dag(self) -> WeightedDAG:
        adj = defaultdict(defaultdict(float))
        for a, b, flow in self.edges():
            if flow.capacity > 0:
                adj[a][b] += flow.capacity
        return WeightedDAG(adj)


@dataclass
class MaxFlow:
    flowdag: FlowDAG
    s: str
    t: str

    def run(self) -> float:
        maxflow = 0
        while True:
            lvls = self.get_levels()
            if lvls[self.t] == 0:
                return maxflow
            while True:
                flow = self.push_flow(lvls)
                if not flow:
                    break
                maxflow += flow

    def get_levels(self) -> defaultdict[str, int]:
        lvls = defaultdict(int)
        queue = deque([self.s])
        while queue:
            v = queue.popleft()
            for neighbor, flow in self.flowdag[v].items():
                if lvls[neighbor] == 0 and flow.free > 0:
                    lvls[neighbor] = lvls[v] + 1
                    queue.append(neighbor)
        return lvls

    def push_flow(self, lvls: defaultdict[str, int]) -> float:
        flow, parents = self.dfs(lvls)
        if self.t not in parents:
            debug("reached blocking flow", indent=1)
            return 0

        path = [self.t]
        while path[-1] != self.s:
            path.append(parents[path[-1]])
        path.reverse()

        debug(f"found path {path} with flow: {flow}", indent=1)
        self.update_residuals(path, flow)
        return flow

    def dfs(self, lvls: defaultdict[str, int]) -> tuple[float, Parents]:
        stack = [(self.s, float("inf"))]
        visited = set()
        parents = dict()
        while stack:
            v, path_flow = stack.pop()
            debug(f"dfs at {v} with path flow {path_flow}", indent=1)
            if v in visited:
                continue
            visited.add(v)
            for neighbor, edge in self.flowdag[v].items():
                debug(f"neighbor {neighbor} has edge flow {edge}", indent=2)
                if neighbor in visited:
                    continue
                is_sink = neighbor == self.t
                is_uplevel = lvls[neighbor] == lvls[v] + 1
                if edge.free > 0 and (is_sink or is_uplevel):
                    parents[neighbor] = v
                    path_flow = min(path_flow, edge.free)
                    if is_sink:
                        return path_flow, parents
                    stack.append((neighbor, path_flow))
        return 0, parents

    def update_residuals(self, path: list[str], flow: float) -> None:
        for i in range(len(path) - 1):
            a, b = path[i], path[i + 1]
            self.flowdag[a][b].flow += flow
            self.flowdag[b][a].flow -= flow


def debug(msg: str, indent: int = 0) -> None:
    if DEBUG:
        print(f"{'\t'*indent}{msg}")
