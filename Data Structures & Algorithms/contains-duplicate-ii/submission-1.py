class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        vis = set()
        l = 0

        for r in range(len(nums)):
            if r - l > k:
                vis.remove(nums[l])
                l += 1
            if nums[r] in vis:
                return True
            vis.add(nums[r])
        return False