import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        a = 1
        b = max(piles)
        best = 1

        while (a <= b):
            k = (a+b)//2

            ans = 0
            for x in piles:
                ans += math.ceil(x/k)

            if ans > h: a = k + 1
            else: 
                best = k
                b = k-1
        
        return best


