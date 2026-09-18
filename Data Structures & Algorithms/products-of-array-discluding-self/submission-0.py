class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = []
        r = []
        temp = 1
        for x in nums:
            temp = temp*x
            l.append(temp)
        temp = 1
        for x in reversed(nums):
            temp = temp*x
            r.append(temp)
        r.reverse()
        ans = []
        
        ans.append(r[1])
        for i in range(1, len(nums)-1):
            ans.append(l[i-1]*r[i+1])
        ans.append(l[len(nums)-2])

        return ans
