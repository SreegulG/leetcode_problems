# Next Greatest Letter Finder

This project provides a Python implementation to find the smallest letter greater than a given target
in a sorted list of letters. The letters list is assumed to wrap around cyclically.

## Logic

- Given a sorted list of letters and a target letter, we want to find the smallest letter that is greater than the target.
- If the target letter is equal to or greater than the last letter in the list, return the first letter (wrap-around).
- Otherwise, perform a binary search:
  - Maintain `start` and `end` pointers.
  - Find the middle index `mid`.
  - If `letters[mid]` is greater than target, discard the right half by setting `end = mid - 1`.
  - Else, discard the left half by setting `start = mid + 1`.
- After the loop, `letters[start]` is the smallest letter greater than the target.

This approach runs in **O(log n)** time due to binary search.


## Features

- Efficient binary search solution.
- Supports wrap-around of letter list.
- Works on any sorted list of lowercase English letters.

## Contributing

Feel free to submit pull requests or suggest improvements!


