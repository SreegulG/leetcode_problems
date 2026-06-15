class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        ans = 0
        curr_sum = 0
        prefix_sum = {0:1}

        for n in nums:
            curr_sum += n
            diff = curr_sum - k
            if diff in prefix_sum:
                ans += prefix_sum[diff]
            prefix_sum[curr_sum] = prefix_sum.get(curr_sum,0) + 1

        return ans
        