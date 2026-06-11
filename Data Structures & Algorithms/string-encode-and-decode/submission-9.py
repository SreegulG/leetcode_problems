class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""
        res = []
        for i in strs:
            res.append(str(len(i)))
            res.append("#")
            res.append(i)
        
        return "".join(res)

    def decode(self, s: str) -> List[str]:
        if not s:
            return []
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            l = int(s[i:j])

            res.append(s[j+1: j+1+l])
            i = j+1+l
        return res