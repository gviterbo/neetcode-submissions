class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        s = {}
        for x in strs:
            temp = "".join(sorted(x))
            if temp not in s:
                s[temp] = [x]
            else: 
                s[temp].append(x)
        ans = []
        for x in s.values():
            ans.append(x)
        return ans
        

        