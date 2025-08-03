class Solution:
    """
    A class containing a method to determine the index at which a target should
    be inserted into a sorted array to maintain sorted order.
    """

    def searchInsert(self, nums, target):
        """
        Find the index of the target in nums, or the index where it can
        be inserted to maintain sorted order.

        Parameters
        ----------
        nums : list of int
            A list of integers sorted in ascending order.
        target : int
            The integer value to search for or insert.

        Returns
        -------
        int
            The index of the target if found; otherwise, the index where the
            target should be inserted.
        """
        start = 0
        end = len(nums) - 1
        while start <= end:
            mid = start + (end - start) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                start = mid + 1
            else:
                end = mid - 1
        return start


# Example usage
sol = Solution()
arr1 = [1, 3, 5, 6]
arr2 = [1, 3, 5, 6]
print(sol.searchInsert(arr1, 5))
print(sol.searchInsert(arr2, 2))
