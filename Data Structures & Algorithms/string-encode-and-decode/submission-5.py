class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return "-1"
        return "é".join(strs)

    def decode(self, s: str) -> List[str]:
        if s == "-1":
            return []
        return s.split("é")