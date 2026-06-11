class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return "-1"
        s = ""
        for i in strs:
            s = s + "ñ" + i
        return s + "ñ"
        

    def decode(self, s: str) -> List[str]:
        if s == "-1":
            return []
        ans = []
        start = 1
        print(s)
        for i in range(1,len(s)):
            if s[i] == "ñ":
                
                ans.append(s[start:i])
                start = i + 1
        return ans