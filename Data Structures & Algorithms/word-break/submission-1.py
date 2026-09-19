class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        

        n = len(s)
        st = set(wordDict)
        ans = [False]*n

        for i in range (n):
            for w in st:
                l = len(w)
                if i-l+1 < 0: 
                    continue
                if s[i-l+1:i+1] in st and (i-l+1 == 0 or ans[i-l]):
                    ans[i] = True
        return ans[n-1]
