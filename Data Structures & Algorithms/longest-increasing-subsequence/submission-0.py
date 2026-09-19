class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        ans = [1]*n
        best = 1
        for i in range(1,n):
            for j in range(i-1, -1, -1):
                if nums[j] < nums[i]:
                    ans[i] = max(ans[i], 1 + ans[j])
                    best = max(best, ans[i])
        return best
                

