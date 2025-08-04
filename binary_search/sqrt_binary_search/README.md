# Integer Square Root via Binary Search

This module implements a fast algorithm to compute the integer part of the square root of a non-negative integer using binary search.

## Problem Logic

- Given an integer x, find the greatest integer y such that y*y <= x.
- Use **binary search** between 1 and x:
  - If mid*mid is less than or equal to x, update the result and search right half for a possibly larger answer.
  - If mid*mid is more than x, search the left half.
- Loop terminates with ans holding the integer square root.

## Complexity Analysis

- **Time Complexity:** O(log x) (because the search range is halved each iteration)
- **Space Complexity:** O(1) (constant extra space)


## Contributions

Contributions and suggestions are very welcome!


