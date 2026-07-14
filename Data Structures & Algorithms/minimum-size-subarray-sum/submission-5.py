class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        window = [nums[0]]
        n = len(nums)
        min_len = 1 if nums[0] >= target else n + 1
        l = 0
        for r in range(1,n):
            window.append(nums[r])
            while sum(window) >= target:
                # print(window)
                min_len = min(min_len,len(window))
                window = window[1:]

        if min_len == n + 1:
            return 0
        return min_len