class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1 = sorted(s1)
        window = set()
        k = len(s1)

        for i in range(0,len(s2)-k+1):
            s3 = s2[i:i+k]
            print(s3,i)
            s3 = sorted(s3)
            if s1 == s3:
                return True
        return False
        