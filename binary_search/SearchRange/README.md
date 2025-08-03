# Find First and Last Position of Element in Sorted Array

This project provides a Python method to find the starting and ending positions of a given target value in a sorted array. If the target is not present, the method returns (-1, -1).

## Problem Logic

- Use binary search twice:
  - One to find the **leftmost (first) occurrence** of the target.
  - Another to find the **rightmost (last) occurrence** of the target.
  
- For the left boundary:
  - Narrow the search space to the left half whenever possible if the current mid element is greater or equal to the target.
  
- For the right boundary:
  - Narrow to the right half whenever possible if mid element is less than or equal to the target.
  
- Both approaches ensure finding the exact first and last indices efficiently.

## Complexity Analysis

- **Time Complexity:** O(log n) — Each binary search runs in logarithmic time; two binary searches overall.
- **Space Complexity:** O(1) — Constant extra space usage.

## Contributing

Feel free to submit pull requests or suggest improvements!
