class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        l = len(nums)

        for i in range(l):
            if nums[i]<=0:
                nums[i] = (l+2)
        print(nums)
        for i in range(l):
            val = abs(nums[i])

            if 1<=val<= l and nums[val-1]>0:
                nums[val-1] *= -1
        print(nums)
        for i in range(1,l+1):
            if nums[i-1]>0:
                return i
        return l+1