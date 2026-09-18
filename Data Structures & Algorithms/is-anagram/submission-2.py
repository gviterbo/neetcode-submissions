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

        for k in ht1.keys():
            if k not in ht2:
                return False
            if ht1[k] != ht2[k]:
                return False
        for k in ht2.keys():
            if k not in ht1:
                return False
            if ht1[k] != ht2[k]:
                return False
        return True
        