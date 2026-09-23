class Solution:
    def lengthOfLastWord(self, s: str) -> int:

        ans = 0
        n = len(s)
        i = n - 1
        first = True
        while i >= 0:
            while s[i] == " " and first:
                i -= 1
            first = False
            if s[i] == " ":
                break
            ans += 1
            i -= 1
        return ans
