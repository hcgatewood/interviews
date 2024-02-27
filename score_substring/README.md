# Score substring

## Problem

Given a string of bits of length n, find the maximum-scored substring.

- The string contains `0` and `1` characters
- The score of a substring is the number of `1` characters minus the number of `0` characters
- Return the score and the indices of the substring

## Solution

This is a variation of the [maximum subarray problem](https://en.wikipedia.org/wiki/Maximum_subarray_problem).

### Naive solution

The naive solution considers all O(n^2) possible substrings, calculating the score of each in O(n). This requires O(n^3) time and O(1) space, incurring an O(n^2) time penalty above linear.

Another naive solution is to convert the string's score deltas to absolute scores, then perform a simplified version of the optimized solution. This requires O(n) time and O(n) space, incurring an O(n) space penalty above constant.

### Optimized solution

The optimized solution computes the absolute score on the fly, rather than precomputing:

- Keep a running total of the absolute score, as well as the lowest absolute score seen so far
- Track the highest absolute score delta (and its indices) seen so far
- Continue to the end of the string

This requires O(n) time and O(1) space.
