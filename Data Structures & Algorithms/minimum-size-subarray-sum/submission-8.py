class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        window = 0
        n = len(nums)
        min_len = n + 1
        l = 0
        for r in range(n):
            window += nums[r]
            while window >= target:
                min_len = min(min_len, r - l + 1)
                window -= nums[l]
                l += 1

        if min_len == n + 1:
            return 0
        return min_len
