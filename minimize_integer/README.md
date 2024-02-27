# Minimize integer

## Problem

Given an integer with n digits, return the minimum integer possible after at most k digit swaps.

- Swaps exchange directly adjacent digits

## Solution

The problem can be solved via a greedy approach, always seeking the smallest reachable digit to move to the front of the integer.

Both algorithms are roughly analogous to performing a [selection sort](https://en.wikipedia.org/wiki/Selection_sort) on the integer  as a list of digits, seeking the max-length prefix of the fully sorted array while halting after at most k swaps.

### Naive solution

The naive solution continually sweeps out as far right as it can to find the smallest reachable digit, then iteratively swapping it to the front. This requires O(n^2) time, as each of the O(n) subproblems takes O(n) time, and O(1) space.

This incurs an O(n) penalty above linear.

### Optimized solution

The optimized solution uses a digit index and [Fenwick tree](https://en.wikipedia.org/wiki/Fenwick_tree) to reduce the cost of finding and swapping a digit. This requires O(n log(n)) time, as each of the O(n) subproblems takes O(log(n)) time, and O(n) space.

In the selection sort analogy, the digit index enables O(1) selection, and the Fenwick tree enables O(log(n)) insertion. Together, they reduce the subproblem from O(n) to O(log(n)).

- Keep an updated mapping of digits to their indices, sorting the indices to access lowest-first
- For each digit, find the smallest reachable digit to the right
- Directly swap the digit to the current front of the integer
- Subtract the cost of the swap from k, but discounted according to a point query of the Fenwick tree
- Update the Fenwick tree to reflect the swap

This incurs only an O(log(n)) penalty above linear, at the cost of O(n) space.

## Resources

- [Fenwick tree (YouTube)](https://www.youtube.com/watch?v=RgITNht_f4Q&list=PLDV1Zeh2NRsB6SWUrDFW2RmDotAfPbeHu&index=38&ab_channel=WilliamFiset)
