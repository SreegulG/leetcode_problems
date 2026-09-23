class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:

        n = len(arr)
        i = n - 2
        ans = [-1] * n
        max_val = float("-inf")

        while i >= 0:
            max_val = max(max_val, arr[i + 1])
            ans[i] = max_val
            i -= 1

        return ans
