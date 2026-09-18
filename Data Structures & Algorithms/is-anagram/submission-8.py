class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        count = [0] * 26

        for x in s:
            count[ord(x) - ord('a')] += 1
        for x in t:
            count[ord(x) - ord('a')] -= 1
        
        for x in count:
            if x != 0:
                return False
        return True
