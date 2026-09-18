class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        ans = []
        for x in s:
            if x.isalnum():
                ans.append(x.lower())
        l = 0
        r = len(ans)-1
        while(l <= r):
            a = ans[l]
            b = ans[r]
            if a != b:
                return False
            else:
                l += 1
                r -= 1
        return True
            
                
    
        