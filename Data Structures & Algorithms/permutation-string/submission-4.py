from collections import defaultdict
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        def check_equal(d1,d2):
            for i in range(26):
                c = chr(ord('a')+i)
                if d1.get(c,0) != d2.get(c,0):
                    return False
            return True

        if len(s1)>len(s2):
            return False
        count1 = defaultdict(int)
        count2 = defaultdict(int)

        for i in range(len(s1)):
            count1[s1[i]] += 1
            count2[s2[i]] += 1
        
        if check_equal(count1,count2):
            return True
        l = 0
        for r in range(len(s1),len(s2)):
            count2[s2[l]] -= 1
            count2[s2[r]] = count2.get(s2[r],0) + 1
            l += 1
            if check_equal(count1,count2):
                return True
        
        return False