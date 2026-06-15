class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        d = defaultdict(int)
        target = len(nums)//3
        ans = []
        for n in nums:
            d[n] += 1

            if len(d)<3:
                continue

            d1 = defaultdict(int)
            for k,v in d.items():
                if v > 1:
                    d1[k] = v- 1
            d = d1

        for n in d:
            if nums.count(n) > target:
                ans.append(n)
        return ans