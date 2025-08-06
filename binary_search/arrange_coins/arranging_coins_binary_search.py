class Solution:
    """
    A class containing a method to determine how many complete staircase rows of coins
    can be formed given n coins, where each ith row has exactly i coins.
    """

    def arrangeCoins(self, n):
        """
        Calculates the maximum number of complete staircase rows that can be formed
        with n coins using binary search.

        Parameters
        ----------
        n : int
            The total number of coins.

        Returns
        -------
        int
            The maximum number of complete rows that can be built.
        """
        start = 0
        end = n
        ans = 0
        while start <= end:
            mid = start + (end - start) // 2
            rows = (mid * (mid + 1)) / 2
            if rows > mid:
                end = mid - 1
            else:
                ans = mid
                start = mid + 1
        return ans


sol = Solution()
print(sol.arrangeCoins(5))
