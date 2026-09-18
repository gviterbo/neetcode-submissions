class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums.sort()
        m = 1
        ma = 0
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                continue
            if nums[i] == nums[i-1] + 1:
                m += 1
            else:
                ma = max(ma, m)
                m = 1
        return max(ma, m)
