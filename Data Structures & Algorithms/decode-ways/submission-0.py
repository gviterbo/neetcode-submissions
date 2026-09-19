class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        nums = set()
        for x in range(1,27):
            nums.add(str(x))
        
        ans = [0]*n
        if s[0] in nums:
            ans[0] = 1

        for i in range(1,n):
            x = 1
            if s[i-1: i+1] in nums:
                if i > 2: x = ans[i-2]
                ans[i] += x
            if s[i] in nums:
                x = ans[i-1]
                ans[i] += x
        return ans[n-1]
            
