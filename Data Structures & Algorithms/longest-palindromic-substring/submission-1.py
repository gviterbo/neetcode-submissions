class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s
        
        ans = [0, 0] 
        n = len(s)
        for i in range(n):
            curr = [i, i]
            l = i-1
            r = i+1
            while l >= 0 and r <= n-1:
                if s[l] == s[r]:
                    curr = [l, r]
                    if r-l > ans[1]-ans[0]: ans = [l, r]
                    l -= 1
                    r += 1
                else:
                    break
            
            if curr[1]-curr[0] > ans[1]-ans[0]: ans = [curr[0], curr[1]] 
        

        for i in range(n-1):
            if s[i] != s[i+1]: 
                continue
            curr = [i, i+1]
            l = i-1
            r = i+2
            while l >= 0 and r <= n-1:
                if s[l] == s[r]:
                    curr = [l, r]
                    if r-l > ans[1]-ans[0]: ans = [l, r]
                    l -= 1
                    r += 1
                else:
                    break
            if curr[1]-curr[0] > ans[1]-ans[0]: ans = [curr[0], curr[1]] 

        return s[ans[0]:ans[1]+1]