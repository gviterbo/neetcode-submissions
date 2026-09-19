class Solution:
    def countSubstrings(self, s: str) -> int:
        total = 0
        n = len(s)

        ans = [[False]*n for _ in range(n)]

        for l in range(n):
            for i in range(n-l):

                if s[i] == s[i+l] and(l<=2 or ans[l-2][i+1]):
                    ans[l][i] = True
                    total += 1
        
        return total

                