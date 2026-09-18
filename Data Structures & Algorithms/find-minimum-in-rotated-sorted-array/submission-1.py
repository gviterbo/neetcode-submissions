class Solution:
    def findMin(self, nums: List[int]) -> int:

        x = nums[0]
        y = nums[-1]
        if x < y: return x

        a = 0
        b = len(nums)-1
        best = nums[b]

        while a <= b:
            k = (a+b)//2
            if nums[k] > nums[b]:
                a = k+1
            else:
                best = min(nums[k],best)
                b = k-1
        return best
            


        