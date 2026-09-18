class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        hm = {}
        for x in nums:
            hm[x] = 1
        
        for x in hm.keys():
            if hm[x] != 1:
                continue
            temp = x
            while(True):
                temp += 1
                if temp in hm:
                    if(hm[temp] >= 2):
                        hm[x] += hm[temp]
                        break
                    else:
                        hm[x] += 1        
                else:
                    break
        
        m = 0
        for x in hm.values():
            m = max(m, x)
        
        return m
        