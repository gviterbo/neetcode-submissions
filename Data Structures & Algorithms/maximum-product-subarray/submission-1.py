class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        dpg = [0]*n
        dpp = [0]*n
        dpg[0] = dpp[0] = nums[0]

        for i in range(1, n):
            temp1 = max(nums[i]*dpp[i-1], max(nums[i]*dpg[i-1],nums[i]))
            temp2 = min(nums[i]*dpp[i-1], min(nums[i]*dpg[i-1],nums[i]))
            dpg[i] = temp1
            dpp[i] = temp2

        return max(dpg)