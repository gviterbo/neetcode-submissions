class Solution:
    def longestPalindrome(self, s: str) -> str:
        index, lengh = 0, 0
        n = len(s)
        ans = [[False]*n for _ in range(n)]

        for l in range(n):
            for i in range(n-l):
                
                if s[i] == s[i+l] and (l<=2 or ans[l-2][i+1]):
                    ans[l][i] = True
                    
                    if lengh <= l:
                        index = i
                        lengh = l
        
        return s[index:index+lengh+1]

        
