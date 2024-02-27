# Find reachable

## Problem

Given an n by k chessboard and a queen's starting position, return the list of reachable cells.

## Solution

The problem can be solved by searching out in each of the queen's 8 possible directions, appending reachable cells until the search is blocked by the edge of the board. This is an example of [iteration](https://en.wikipedia.org/wiki/Iteration); an analogous solution could also use [recursion](https://en.wikipedia.org/wiki/Recursion).

Assuming wlog that O(n) >= O(k), this requires O(n) time and O(1) auxiliary space (with O(n^2) for the input and O(n) for the output).
