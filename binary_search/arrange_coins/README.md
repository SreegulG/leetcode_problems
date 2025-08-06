# Arranging Coins (LeetCode 441)

Given `n` coins, the task is to build a staircase with these coins, consisting of complete rows where the ith row has exactly i coins. The goal is to return the total number of completely formed staircase rows.

## Logic

- The ith row requires exactly i coins, so the total coins needed to form k complete rows is `k*(k+1)/2`.
- The problem reduces to finding the largest integer k such that `k*(k+1)/2 <= n`.
- This can be solved efficiently with binary search:
  - Use `start = 0` and `end = n` as the search bounds.
  - For each `mid`, if `mid*(mid+1)/2 <= n`, try to increase `mid`; otherwise, decrease it.
  - The process narrows down to the maximal complete row count.

## Complexity Analysis

- **Time Complexity:** O(log n)  
  Binary search halves the search range on each iteration.
- **Space Complexity:** O(1)  
  Only a constant number of variables are used.

## Example

With `n = 5`:
- Row 1 needs 1 coin (4 left)
- Row 2 needs 2 coins (2 left)
- Row 3 needs 3 coins (but only 2 remain, can't form this row)
- So, the answer is 2 complete rows.


## Contribution

Contributions, issues, and suggestions are welcome!


