class Solution:
    """
    A class that provides an efficient method to compute the integer square root of a number.
    """

    def mySqrt(self, x: int) -> int:
        """
        Compute and return the integer square root of a non-negative integer x.
        The integer square root is the greatest integer y such that y*y <= x.

        Uses binary search to achieve logarithmic time complexity.

        Parameters
        ----------
        x : int
            The non-negative integer to compute the square root of.

        Returns
        -------
        int
            The integer part of the square root of x.
        """
        if x == 0 or x == 1:
            return x

        start = 1
        end = x
        ans = x  # To store result

        while start <= end:
            mid = start + (end - start) // 2
            if mid * mid > x:
                # If mid^2 is too large, search the left half
                end = mid - 1
            else:
                # If mid^2 is less than or equal to x, update answer and search right half
                ans = mid
                start = mid + 1

        return ans


# Example usage
sol = Solution()
print(sol.mySqrt(8))  # Output: 2
print(sol.mySqrt(16))  # Output: 4
