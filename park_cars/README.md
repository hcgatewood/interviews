# Park cars

## Problem

Given n cars' locations, find the minimum fuel required to park them all to a common lot.

- Locations are specified as (x,y) coordinates in the 2D plane
- Input is sorted by x-coordinate
- Cars must be parked horizontally (parallel to the x-axis), at unique locations, and with 1 unit of space between each car
- Calculate fuel costs as Manhattan distance

## Solution

Solutions require 3 insights:

1. Manhattan distance metric allows independent cost calculations per axis
2. For y-axis: the median value of y minimizes y-axis cost
3. For x-axis: the median value of x_i - i for the left-most parked car minimizes x-axis cost

Explanation for x-axis:

- Beginning with car_0 at x=0, place each car_i at i (default starting point)
- Cost for car_i becomes abs(x_i - i)
- Because the cost function is linear, we can minimize the total cost by minimizing the median individual cost
- So select the median value of x_i - i, then shift each car's position by that value

With that in hand, solutions reduce to efficiently finding medians.

### Naive solution

The naive solution calculates medians by sorting then selecting the middle element. This requires O(n log(n)) time.

This incurs an O(log(n)) penalty above linear.

### Optimized solution

The optimized solution calculates medians via quickselect. This requires O(n) time.

This particular solution does not provide pivot selection guarantees, so runtime is only expected O(n). However, it is possible to guarantee O(n) time using the [median of medians](https://en.wikipedia.org/wiki/Median_of_medians) method for pivot selection.
