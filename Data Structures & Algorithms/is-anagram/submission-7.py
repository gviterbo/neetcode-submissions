class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        hms, hmt = {}, {}

        for x in s:
            hms[x] = 1 + hms.get(x, 0)
        for x in t:
            hmt[x] = 1 + hmt.get(x, 0)
        
        return hms == hmt