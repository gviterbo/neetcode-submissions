class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        s = {}
        for x in strs:
            l = [0] * 26
            for c in x:
                l[ord(c) - ord('a')] += 1
            s.setdefault(str(l), []).append(x)
        
        return list(s.values())
        