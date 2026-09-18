class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm  = {}
        size = {}
        for i in range(len(nums)):
            if nums[i] not in hm:
                hm[nums[i]] = i
            size[nums[i]] = 1 + size.get(nums[i], 0)

        for x in nums:
            if x == target - x:
                if size[x] == 1: continue
                else:
                    ans = []
                    for i in range(len(nums)): 
                        if nums[i] == x:
                            ans.append(i)
                    return ans

            elif target - x in hm.keys():
                m = min(hm[x], hm[target - x])
                M = max(hm[x], hm[target - x])
                return [m, M]

        