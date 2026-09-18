class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ht1 = {}
        ht2 = {}
        for x in s:
            if x not in ht1:
                ht1[x] = 1
            else: 
                ht1[x] += 1
        for x in t:
            if x not in ht2:
                ht2[x] = 1
            else:
                ht2[x] += 1

        return ht1 == ht2
        