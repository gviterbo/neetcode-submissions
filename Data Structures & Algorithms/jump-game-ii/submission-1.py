class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        n = len(nums)
        ans = 1
        prev = nums[0]
        curr = nums[1]+1

        for i in range(2, n):
            temp = nums[i]+i
            if prev < i:
                prev = curr
                ans += 1
            curr = max(curr, temp)
        return ans



        