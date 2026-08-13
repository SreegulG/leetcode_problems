class Solution:

    def encode(self, strs: List[str]) -> str:
        ans = []
        for word in strs:
            ans.append(str(len(word)))
            ans.append("#")
            ans.append(word)
            
        return "".join(ans)

    def decode(self, s: str) -> List[str]:
        ans = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            
            ans.append(s[j + 1: length + j + 1])
            i = length + j + 1

        return ans
