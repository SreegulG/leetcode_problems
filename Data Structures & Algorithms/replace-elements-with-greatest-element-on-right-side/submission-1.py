class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:

        n = len(arr)
        i = n - 1
        max_val = -1

        while i >= 0:
            curr_max = max(max_val, arr[i])
            arr[i] = max_val
            max_val = curr_max
            i -= 1

        return arr
