class Solution:
    """
     A class containing a method to perform binary search on a sorted list.
     """

    def search(self, nums, target):
        """
        Search for a target value in a sorted list using binary search.

        Parameters
        ----------
        nums : list of int
            A list of integers sorted in ascending order.
        target : int
            The integer value to search for.

        Returns
        -------
        int
            The index of the target if it is found; otherwise, -1.
        """
        start = 0
        end = len(nums) - 1
        while start <= end:
            mid = start + (end - start) // 2
            if nums[mid] > target:
                end = mid - 1
            elif nums[mid] < target:
                start = mid + 1
            else:
                return mid
        return -1


# Example usage
sol = Solution()
arr = [-1, 0, 3, 5, 9, 12]
print(sol.search(arr, 9))
