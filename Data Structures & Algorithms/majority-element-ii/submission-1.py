class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        d = defaultdict(int)
        target = len(nums)//3
        ans = []
        for n in nums:
            d[n] += 1
        
        for key,val in d.items():
            if val > target:
                ans.append(key)
        return ans