class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        vs1 = [0]*26
        vs2 = [0]*26

        for x in s1:
            vs1[ord(x)-ord('a')] += 1
    
        for i in range(len(s1)):
            x = s2[i]
            vs2[ord(x)-ord('a')] += 1
        l = 0
        for r in range(len(s1), len(s2)):
            x = s2[l]
            y = s2[r]
            if vs1 == vs2: 
                return True
            else:
                vs2[ord(x) - ord('a')] -= 1
                vs2[ord(y) - ord('a')] += 1
                l += 1
        return vs1 == vs2

        