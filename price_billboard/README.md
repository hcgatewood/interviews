# Price billboard

## Problem

Find the cost of a word, given an alphabet of size n and a map of k known costs for other words.

- Motivating example: imagine buying a billboard with your company's name, and you want to know the price of your billboard given the price of other companies' billboards
- A word's cost is the sum of the costs of its characters
- If the cost can't be found, return None

## Solution

This is a linear algebra problem, requiring solving a system of linear equations. In either solution, numpy will provide the underlying linear algebra operations.

### Naive solution

The naive solution tries to find the individual cost of each letter.

- Set A to the matrix of known word frequencies. Each column is a letter, each row is a known word.
- Set b to the cost of each known word
- Solve for x
- Set y to the frequency vector of the unknown word
- The cost of the known word is the dot product of x and y

```
known_prices = {"ab": 10, "cde": 15, "ee": 10}
A = [
#    a  b  c  d  e
    [1, 1, 0, 0, 0], # ab
    [0, 0, 1, 1, 1], # cde
    [0, 0, 0, 0, 2], # ee
]
b = [
    10, # ab
    15, # cde
    10, # ee
]

unknown_word = "abcd"
#    a  b  c  d  e
y = [1, 1, 1, 1, 0]
```

This requires O(kn^2) time and O(kn) space, as A has k rows and n columns.

The issue with this approach is that it returns false negatives. Specifically, there are cases where the cost of the unknown word can be found even when the cost of each individual letter cannot. The example above is one such case.

### Optimized solution

Instead of trying to find the cost of each letter, the optimized solution finds the combination of known words that equals the unknown word.

- Set A to the matrix of known word frequencies. Each column is a known word, each row is a letter. (Side note: this is the transpose of the naive solution's A.)
- Set b to the vector of the unknown word's frequencies
- Solve for x
- Set y to the vector of known word prices
- The cost of the known word is the dot product of x and y

```
known_prices = {"ab": 10, "cde": 15, "ee": 10}
A = [
#   ab cde e
    [1, 0, 0], # a
    [1, 0, 0], # b
    [0, 1, 0], # c
    [0, 1, 0], # d
    [0, 1, 2], # e
]
unknown_word = "abcd"
#    a  b  c  d  e
b = [1, 1, 1, 1, 0]

y = [10, 15, 10]
```

This requires O(nk^2) time and O(nk) space, as A has n rows and k columns.

## Alternative solutions

### Superfluous known words

In the case where k >> n, the optimized solution can be modified to remove superfluous known words.

- Set A as the same matrix as before, but initially as an n x 0 matrix
- Index known words by their letters
- Iterate over each letter in the unknown word, find a known word that contains the letter, and concatenate it to A if it's linear independent of the existing columns of A
- Repeat until rank(A|b) = rank(A)

In the worst case, this requires O(nk^3) time, but in practice will be closer to O(n^4) time, assuming the known words are not intentionally chosen to be linearly dependent. So for O(k) > O(n^(3/2)), and generally linearly independent known words, this is an improvement over the optimized solution.

### Superfluous alphabet

In the case where n >> k, the optimized solution can be modified to remove superfluous letters, analogous to the above.
