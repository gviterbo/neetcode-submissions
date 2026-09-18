class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        ll = 0
        rr = len(height) - 1
        r = len(height) - 1
        ans = 0
        while(l < r):
            
            hl = height[l]
            hr = height[r]

            if (height[ll] < height[rr]):
                if (height[ll] >= hl):
                    ans += height[ll] - hl
                    l += 1
                else: 
                    ll = l
            else: 
                if (height[rr] >= hr):
                    ans += height[rr] - hr
                    r -= 1
                else: 
                    rr = r
        return ans