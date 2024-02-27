from dataclasses import astuple, dataclass
from typing import Generic, NamedTuple, Optional, TypeVar

from lib import defaultdict


@dataclass
class Loan:
    creditor: str
    debtors: dict[str, float]

    def __lt__(self, them):
        return self.creditor < them.creditor


@dataclass
class Repayment:
    debtor: str
    creditors: dict[str, float]

    def __lt__(self, them):
        return self.debtor < them.debtor


@dataclass
class FlowWeight:
    flow: float
    capacity: float

    @property
    def free(self) -> float:
        return self.capacity - self.flow

    def __str__(self):
        return f"{self.flow}/{self.capacity}={self.free}"

    def __repr__(self):
        return str(self)

    def __hash__(self):
        return hash(astuple(self))

    def __bool__(self):
        return self.capacity > 0


Weight = TypeVar("Weight", float, FlowWeight, None)


class Edges(defaultdict[str, Weight], Generic[Weight]):
    pass


Parents = dict[str, str]


class Edge(NamedTuple, Generic[Weight]):
    start: str
    end: str
    weight: Optional[Weight]

    def __str__(self):
        return f"({self.start} -> {self.end}: {self.weight})"

    def __repr__(self):
        return str(self)

    def __bool__(self):
        return self.weight is not None and bool(self.weight)
