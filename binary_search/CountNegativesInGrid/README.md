# Count Negative Numbers in a Sorted 2D Grid

This project contains an efficient Python solution to count the number of negative numbers
in a 2D grid where each row and each column is sorted in non-increasing order (descending).

## Problem Description

Given a grid where:
- Each row is sorted in descending order.
- Each column is sorted in descending order.

The task is to count how many negative numbers are present in the entire grid.

## Solution Logic

- We start from the **bottom-left** corner (last row, first column).
- While inside grid boundaries:
  - If the current element is negative, since rows are sorted descending,
    all elements to the right of the current column in this row are also negative.
    - Add all those to the count.
    - Move **up one row**.
  - Else, move **right one column**.
- Continue until we move out of the grid.

This approach ensures we only move at most `m + n` steps (where `m` = #rows, `n` = #columns).

## Complexity Analysis

- **Time Complexity:**  
  O(m + n) — We traverse at most one full column and one full row.

- **Space Complexity:**  
  O(1) — The algorithm uses constant extra space.

## Contributing

Pull requests are welcome!

