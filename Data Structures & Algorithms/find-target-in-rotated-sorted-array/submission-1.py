class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        x = nums[0]
        y = nums[-1]
        index = -1
        if x < y: 
            index = 0
        else: 
            a = 0
            b = len(nums)-1
            best = nums[-1]
            index = b
            while a <= b:
                k = (a+b)//2
                if nums[k] > nums[b]:
                    a = k+1
                else:
                    if best > nums[k]:
                        best = nums[k]
                        index = k
                    b = k-1
        a = 0
        b = len(nums)-1
        if nums[index] <= target and target <= nums[-1]:
            a = index
            b = len(nums)-1
        else:
            a = 0
            b = index-1
        
        while(a<=b):
            k = (a+b)//2
            if nums[k] == target:
                return k
            if nums[k] < target:
                a = k + 1
            else:
                b = k - 1
        return -1

        
