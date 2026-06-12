class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [1]*(n+1)
        suffix = [1]*(n+1)
        print(prefix,suffix)

        for i in range(1, n):
            prefix[i] = prefix[i-1]*nums[i-1]
            print(i,n-i-1,n)
            suffix[n-i-1] = suffix[n-i]*nums[n-i] 
        print(prefix,suffix)
        for i in range(n):
            nums[i] = prefix[i]*suffix[i]
        return nums