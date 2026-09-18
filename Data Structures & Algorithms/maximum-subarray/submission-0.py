class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        best = curr = nums[0]
        for i in range(1, len(nums)):
            x = nums[i]
            curr = max(x, x+curr)
            best = max(best, curr)
        return best
        