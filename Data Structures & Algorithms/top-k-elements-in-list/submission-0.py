class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        n = len(nums)
        ans = []
        freq = [[] for _ in range(n+1)]

        for val in nums:
            count[val] = count.get(val,0) + 1

        for key,val in count.items():
            freq[val].append(key)

        for i in range(n,-1,-1):
            for j in freq[i]:
                ans.append(j)
                if len(ans) == k:
                    return ans

