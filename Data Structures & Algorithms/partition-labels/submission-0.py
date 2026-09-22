class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        
        hm = {}

        for i in range(len(s)):
            x = s[i]
            if x not in hm.keys():
                hm[x] = [i,i]
            else:
                hm[x][1] = i
        
        l = []
        l.extend(hm.values())
        l.sort()
        short = l[0][0]
        long = l[0][1]
        ans = []
        for i in range(1, len(l)):
            if l[i][0] > long:
                ans.append(long-short+1)
                short = l[i][0]
            long = max(l[i][1], long)
        ans.append(long-short+1)
        return ans
            

