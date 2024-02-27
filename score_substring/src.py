"""
Given a string of bits, find the maximum-scored substring.
"""

Score = int
Bounds = tuple[int, int]


def score_substring(s: str) -> (Score, Bounds):
    min_score = 0
    min_score_idx = -1
    max_delta = 0
    max_delta_idxs = (0, 0)
    score = 0
    for i, c in enumerate(s):
        score = score + 1 if c == "1" else score - 1
        if score <= min_score:
            min_score = score
            min_score_idx = i
        if score - min_score > max_delta:
            max_delta = score - min_score
            max_delta_idxs = (min_score_idx + 1, i + 1)
    return max_delta, max_delta_idxs
