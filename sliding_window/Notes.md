# Sliding window

## Description

- Used in Places where O(n^2) to process in O(n).
- Subarray, substrings, max, min.

## Core idea

- A window [left, right].
- Expand right.
- Shrink left based on condition or size of window.
- Inside each window calculate computation -> store in set or map -> cross check avoid recomputation.

## Types

- Fixed: window size = k if size >=k remove from left.
- Dynamic: window grows on right until condition is invalid, if valid -> remove left until valid.

## Problems & Learnings

- Contains Duplicate II
  - k=3 window size is 4 cause arrays are 0 indexed.
  - Store the values in set and compare in every loop to avoid recomputation.
