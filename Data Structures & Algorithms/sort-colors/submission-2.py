class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        colours = {0:0,1:0,2:0}

        for val in nums:
            colours[val] += 1
        
        i = 0
        for val in colours:
            while colours[val] > 0:
                nums[i] = val
                colours[val] -= 1
                i += 1