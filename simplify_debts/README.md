# Simplify debts

## Problem

Given a list of k loans among n people, find the minimal set of transactions required to settle all debts.

[Splitwise](https://splitwise.com/) provides the following [requirements](https://www.quora.com/What-algorithm-or-solution-do-the-people-at-Splitwise-use-for-its-debt-simplification-feature) for debt simplification:

1. Everyone owes the same net amount as before
2. No one owes a person they didn't owe before
3. No one owes out more money than they did before

## Solution

See [this Medium article](https://medium.com/@mithunmk93/algorithm-behind-splitwises-debt-simplification-feature-8ac485e97688) for an overview.


### Greedy solution

The greedy solution accumulates the transactions into a net balance for each person, then uses a greedy algorithm to settle the debts.

This requires O(k + n) time, and results in at most n-1 transactions.

This solution is more suitable for live interviews.

The issue with this approach is it ignores requirement #2, and is not guaranteed to minimize the number of transactions.

### Improved solution

The improved solution tries to match payments between subsets of the group, such that the net balance of each subset is zero.

This solution is NP-complete, reducing to the [subset-sum problem](https://en.wikipedia.org/wiki/Subset_sum_problem). Polynomial-time approximations algorithms exist, but exact algorithms require exponential or pseudo-polynomial time.

The result is still at most n-1 transactions, but the number of transactions is guaranteed to be minimized.

As before, the issue with this approach is it ignores requirement #2.

### Full solution

To account for requirement #2, the full solution reduces to solving O(k) [max-flow problems](https://en.wikipedia.org/wiki/Maximum_flow_problem).

- Accumulate the transactions into a DAG, where each vertex is a person and each weighted edge indicates source owes sink the weight
- For each edge in the DAG, push the maximum flow from source to sink over the edge, pruning relevant edges after each max-flow calculation
- Transform back into a list of transactions

Assuming wlog that O(E) >= O(V), and using [Dinic's algorithm](https://en.wikipedia.org/wiki/Dinic%27s_algorithm) to find max-flow, this requires O(V^2 E^2) time, for V vertices/people and E edges in the DAG.

- If O(k) = O(E), this results in O(k^2 n^2) time
- If O(k) > O(E), this results in O(n^6) time
- Practically, it's possible to imagine each user having max O(1) connections, resulting in O(min{n,k}^4) time

## Resources

- Simplify debts
    - [Overview](https://medium.com/@mithunmk93/algorithm-behind-splitwises-debt-simplification-feature-8ac485e97688)
    - Additional treatments [(1)](https://medium.com/@hsharma1456/how-does-the-splitwise-algorithm-work-dc1de5eaa371) [(2)](https://antoncao.me/blog/splitwise) [(3)](https://terbium.io/2020/09/debt-simplification/) [(4)](https://www.researchgate.net/publication/220396130_Settling_Multiple_Debts_Efficiently_An_Invitation_to_Computing_Science)
    - [Constraints](https://www.quora.com/What-algorithm-or-solution-do-the-people-at-Splitwise-use-for-its-debt-simplification-feature)
- Flow algorithms
    - [Overview (YouTube playlist)](https://www.youtube.com/playlist?list=PLDV1Zeh2NRsDj3NzHbbFIC58etjZhiGcG)
    - [Maximum flow problem (Wikipedia)](https://en.wikipedia.org/wiki/Maximum_flow_problem)
    - [Dinic's algorithm (Wikipedia)](https://en.wikipedia.org/wiki/Dinic%27s_algorithm)
