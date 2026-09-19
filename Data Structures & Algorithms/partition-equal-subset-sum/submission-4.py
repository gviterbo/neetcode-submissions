class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        s = sum(nums)
        if s % 2 == 1: 
            return False

        s = s//2
        ans = [[False]*(s+1) for _ in range(n)]
        for i in range(n):
            ans[i][0] = True
        ans[0][nums[0]] = True
        for i in range(1, n):
            
            for x in range(s+1):

                if x-nums[i] < 0:
                    continue
                ans[i][x] = ans[i-1][x-nums[i]] or ans[i-1][x]
                if x == s and ans[i][x]:
                    return True

        return False



        