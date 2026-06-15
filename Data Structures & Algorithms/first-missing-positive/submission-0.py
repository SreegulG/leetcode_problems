class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:

        min_val = 1
        while True:
            if min_val not in nums:
                return min_val
            min_val += 1
        