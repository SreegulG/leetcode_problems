class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ans = 0
        cons_one = 0
        for i, n in enumerate(nums):
            if n:
                cons_one += 1
                ans = max(ans, cons_one)
            else:
                cons_one = 0

        return ans
