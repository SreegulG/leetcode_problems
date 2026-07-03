class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_l = 0
        window = []

        for i in s:
            while i in window:
                del window[0]
            window.append(i)
            max_l = max(max_l,len(window))
        
        return max_l