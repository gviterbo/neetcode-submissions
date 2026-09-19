class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        bag = nums[0]
        for i in range(len(nums)-1):
            bag = max(nums[i],bag-1)
            if bag == 0:
                return False
        return True
