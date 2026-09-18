class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])

        ans = [0]*(len(nums)-1)
        dp = [0]*(len(nums)-1)
        ans[0] = nums[0]
        ans[1] = max(nums[0], nums[1])
        dp[0] = nums[1]
        dp[1] = max(nums[1], nums[2])

        for i in range(2, len(nums)-1):
            ans[i] = max(ans[i-1], ans[i-2]+nums[i])
        for i in range(2, len(nums)-1):
            dp[i] = max(dp[i-1], dp[i-2]+nums[i+1])
        
        return max(dp[-1], ans[-1])
        