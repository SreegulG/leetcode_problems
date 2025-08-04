# Guess Number Higher or Lower (Binary Search)

This module solves the classic "Guess Number Higher or Lower" problem using efficient binary search.

## Problem Logic

- The problem provides a `guess(num)` API for comparison with the hidden picked number.
- The algorithm maintains `start` and `end` pointers to represent the current search interval.
- Repeatedly bisect the interval using `mid = (start + end) // 2` and call `guess(mid)`:
  - If guess is correct (`0`), return `mid`.
  - If guess is too high (`-1`), search lower half (`end = mid - 1`).
  - If guess is too low (`1`), search upper half (`start = mid + 1`).

This binary search swiftly narrows the possibilities to find the picked number.

## Complexity Analysis

- **Time Complexity:** O(log n) — Binary search reduces range by half on each step.
- **Space Complexity:** O(1) — Uses constant additional space.


## Contributions

Feel free to contribute improvements or alternative approaches!


