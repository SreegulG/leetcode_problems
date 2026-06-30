class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        for x in range(1,k+1):
            i = 0
            j = x
            while j<n:
                if nums[i] == nums[j]:
                    return True
                i += 1
                j += 1
        return False