class Solution:
    def rob(self, nums: List[int]) -> int:
        ans = [0]*len(nums)
        if len(nums) == 1:
            return nums[0]
        ans[0] = nums[0]
        ans[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            ans[i] = max(ans[i-1], ans[i-2]+nums[i])

        return ans[len(nums)-1]
        