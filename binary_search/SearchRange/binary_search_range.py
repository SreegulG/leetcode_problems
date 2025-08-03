class Solution:
    """
    A class containing a method to find the starting and ending position of a given target
    value in a sorted list of integers using binary search.
    """
    def searchRange(self, nums, target):
        """
        Find the starting and ending index of a target value in a sorted array.

        Parameters
        ----------
        nums : List[int]
            A list of integers sorted in ascending order.
        target : int
            The target integer to find the range for.

        Returns
        -------
        Tuple[int, int]
            A tuple containing the first and last positions of the target in the list.
            If the target is not found, returns (-1, -1).
        """
        def find_left(nums, target):
            """
            Binary search to find the leftmost (first) index of the target.
            """
            start, end = 0, len(nums) - 1
            left_idx = -1
            while start <= end:
                mid = start + (end - start) // 2
                if nums[mid] < target:
                    start = mid + 1
                else:
                    if nums[mid] == target:
                        left_idx = mid
                    end = mid - 1
            return left_idx

        def find_right(nums, target):
            """
            Binary search to find the rightmost (last) index of the target.
            """
            start, end = 0, len(nums) - 1
            right_idx = -1
            while start <= end:
                mid = start + (end - start) // 2
                if nums[mid] > target:
                    end = mid - 1

                else:
                    if nums[mid] == target:
                        right_idx = mid
                    start = mid + 1
            return right_idx

        return find_left(nums, target), find_right(nums, target)


sol = Solution()
arr = [5, 7, 7, 8, 8, 10]
print(sol.searchRange(arr, 7))
