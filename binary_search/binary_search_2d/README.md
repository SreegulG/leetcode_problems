# Search a 2D Matrix

This module implements an efficient search method in a 2D matrix that satisfies the following conditions:
- Integers in each row are sorted from left to right.
- The first integer of each row is greater than the last integer of the previous row.

## Problem Logic

- Treat the matrix as a flattened sorted list with length = rows * columns.
- Use binary search on this virtual list:
  - Compute the middle index `mid`.
  - Convert `mid` to 2D matrix indices as:
    - row = mid // number_of_columns
    - col = mid % number_of_columns
  - Compare the element at `matrix[row][col]` with the target.
  - Narrow the search range accordingly.

## Complexity

- **Time Complexity:** O(log(m * n)), where `m` is rows and `n` is columns.
- **Space Complexity:** O(1).


## Contribution

Contributions and improvements are welcome!


