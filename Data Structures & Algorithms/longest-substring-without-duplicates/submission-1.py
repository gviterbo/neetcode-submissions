class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        hm = {}
        ans = 0
        for j in range(len(s)):
            x = s[j]
            if x in hm:
                temp = l
                l = hm[x] + 1
                for i in range(temp,hm[x] + 1):
                    hm.pop(s[i])
                hm[x] = j
            else:
                hm[x] = j
                ans = max(ans, j-l+1)
        return ans


        