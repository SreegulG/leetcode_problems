class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numbers = set(nums)
        longest = 0

        for n in numbers:
            if n - 1 not in numbers:
                l = 0
                while n + l in numbers:
                    l += 1
                longest = max(l,longest)
        return longest