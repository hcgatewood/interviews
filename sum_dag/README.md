# Sum DAG

## Problem

Build a [weighted](https://en.wikipedia.org/wiki/Graph_(discrete_mathematics)#Weighted_graph) DAG with n vertices given an online list of leaf values and edges. For each vertex, report the sum of its descendants.

## Solution

Build the DAG as edges are added, calculating sums either on the fly or by caching them.

### Write-optimized solution

The write-optimized solution calculates a sum on-read across all descendants by walking the sub-DAG rooted at the updated vertex.

- Queries: O(n) time and auxiliary space
- Updates: O(1) time and auxiliary space

### Read-optimized solution

The read-optimized solution caches sums on-write across all ancestors by walking the reverse-sub-DAG rooted at the updated vertex.

- Queries: O(1) time and auxiliary space
- Updates: O(n) time and auxiliary space
