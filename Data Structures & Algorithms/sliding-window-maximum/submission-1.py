import heapq

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        max_index = 0
        m = -10001
        ans = []
        for i in range(k):
            if m <= nums[i]:
                m = nums[i]
                max_index = i
        ans.append(m)
        l = 0

        for r in range(k, len(nums)):
            l += 1
            if l > max_index: 
                m = -10001
                for j in range(l, r+1):
                    if m <= nums[j]:
                        m = nums[j]
                        max_index = j
            else:
                if m <= nums[r]:
                    m = nums[r]
                    max_index = r
            ans.append(m)
        return ans

            
        