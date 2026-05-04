# Sliding Window Pattern

## Core Idea

- Maintain a window `[left, right]`
- Convert O(n²) → O(n)
- Avoid recomputation by updating state incrementally

---

## Key Principles

- Right pointer always expands
- Left pointer adjusts only when constraint breaks
- Maintain a running state (set, map, sum, etc.)
- Never recompute full window unless learning/debugging

---

## Types of Sliding Window

### 1. Fixed Window

- Window size = `k`
- Expand right
- Shrink left when size exceeds `k`

**Used in:**

- sum of subarray size k
- max/min in window
- averages

---

### 2. Variable Window

- Expand right until condition breaks
- Shrink left until condition becomes valid again

**Used in:**

- longest substring problems
- frequency-based constraints
- dynamic range problems

---

## Problems and Patterns

### Contains Duplicate II

- Condition: elements within distance ≤ k
- Use sliding window set
- Maintain at most k elements in the set
- Remove leftmost element when window exceeds size

---

### Longest Harmonious Subsequence

- NOT a subarray problem
- Based on frequency map
- Condition: `freq[x] + freq[x+1]` is maximized
- Difference between values is exactly 1

---

### Defuse the Bomb

- Circular array problem
- Fixed window size = `abs(k)`
- `k > 0` → take next k elements
- `k < 0` → take previous k elements
- Always access using circular indexing:index = (start + j) % n
- The index = (start + j) % n solves the out of bounds index issue example - `[5, 7, 1, 4], start = 3, j = 2 → (3 + 2) % 4 = 1 → 7`
- This way window moves around the array in loop.
