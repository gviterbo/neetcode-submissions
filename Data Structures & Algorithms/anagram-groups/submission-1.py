class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        s = {}
        for x in strs:
            temp = "".join(sorted(x))
            s.setdefault(temp, []).append(x)
        
        return list(s.values())