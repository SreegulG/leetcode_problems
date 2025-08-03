# Binary Search Algorithm in Python

This project provides a simple implementation of the binary search algorithm using a Python class. Binary search is a fast, efficient algorithm for finding the position of a target element within a sorted list.

## Logic of the Solution

The binary search algorithm works as follows:
- Begin with two pointers, `start` and `end`, representing the bounds of the sorted search array.
- While `start` is less than or equal to `end`:
  - Calculate the middle index: `mid = start + (end - start) // 2`.
  - If `nums[mid]` equals the target value, return `mid`.
  - If `nums[mid]` is less than the target, adjust `start = mid + 1` to search the right half.
  - If `nums[mid]` is greater than the target, adjust `end = mid - 1` to search the left half.
- If the target value is not found, return `-1`.

This process halves the search space with each iteration, giving binary search a time complexity of **O(log n)**, where n is the number of elements in the list. The algorithm only works correctly on lists that are already sorted.

## Features

- Efficient O(log n) search time
- Returns the index of the target if found, or -1 if not found
- Handles any sorted integer list


