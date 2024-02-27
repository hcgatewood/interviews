# Merge intervals

## Problem

Given k sorted lists of O(n) intervals, merge them into a single sorted list of O(nk) intervals.

- Each interval is a pair of integers [start, end]
- Intervals are sorted by start time
- Merge overlapping intervals as necessary

## Solution

Merging two sorted lists can be done with a two-pointer approach. The focus here is extending to k lists.

### Naive solution

The naive solution merges the lists one-by-one. This requires O(nk^2) time, as each of the O(nk) subproblems takes O(k) time.

This incurs an O(k) penalty above linear.

### Optimized solution

The optimized solution uses a min-heap of size k:

- Add each list of intervals to the heap, indexed by the start time of the first interval in the list
- Pop the min (earliest) list, yield its min (earliest) interval, then advance the list to its next interval and reinsert into the heap if not exhausted
- Repeat until the heap is empty

This requires O(nk log(k)) time, as each of the O(nk) subproblems takes O(log(k)) time.

This incurs an O(log(k)) penalty above linear.

## Alternative solutions

### Unsorted lists

If the lists are not sorted, consider the following

- Presort in O(nk log(nk)): sort each of the O(k) lists in O(n log(n)) time, then use the optimized solution (sum the two time complexities together)
- Flat min-heap in O(nk log(nk)): insert each of the O(nk) intervals into the min-heap in O(log(nk)) time (rather than inserting the lists), then pop the min interval until the heap is empty

Each of these incurs an O(log(nk)) penalty above linear.
