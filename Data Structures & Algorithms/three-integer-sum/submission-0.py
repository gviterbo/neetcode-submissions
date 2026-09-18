class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = set()
        nums.sort()
        for i in range(len(nums)):
            target = nums[i]*(-1)
            l = 0
            r = len(nums)-1
            while(l < r):
                if l == i:
                    l += 1
                    continue
                if r == i:
                    r -= 1
                    continue
                a = nums[l]
                b = nums[r]
                if a + b == target:
                    ans.add(tuple(sorted([a,b,nums[i]])))
                    l += 1
                    r -= 1
                elif a + b < target:
                    l += 1
                else:
                    r -= 1
        final = []

        for x in ans:
            final.append(list(x))
        return final



                
