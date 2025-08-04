# The guess API is assumed to be defined elsewhere:
# def guess(num: int) -> int:
#     Returns -1 if num is higher than the picked number,
#     Returns 1 if num is lower than the picked number,
#     Returns 0 if num is equal to the picked number.

class Solution:
    """
    A class to implement the guess number higher or lower game using binary search.
    """

    def guessNumber(self, n: int) -> int:
        """
        Use binary search to find the picked number between 1 and n,
        using the external `guess` API.

        Parameters
        ----------
        n : int
            The upper limit of the number range (inclusive).

        Returns
        -------
        int
            The correct number picked.
        """
        start = 1
        end = n

        # Binary search for the correct number
        while start <= end:
            mid = start + (end - start) // 2
            guess_val = guess(mid)
            if guess_val == 0:
                return mid  # Found the correct number
            elif guess_val == -1:
                end = mid - 1  # Target is lower
            else:  # guess_val == 1
                start = mid + 1  # Target is higher


pick = 6


def guess(n):
    if n == pick:
        return 0
    if n > pick:
        return -1
    if n < pick:
        return 1


# Example usage
sol = Solution()
print(sol.guessNumber(10))
