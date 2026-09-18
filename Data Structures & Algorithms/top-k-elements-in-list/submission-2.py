class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = [set() for _ in range(len(nums)+1)]
        hm = {}
        for x in nums:
            hm[x] = hm.get(x, 0) + 1
        for x in nums: 
            freq[hm[x]].add(x)
        
        ans = []

        for x in reversed(freq):
            for y in x: 
                if (k == 0):
                    return ans
                ans.append(y)
                k -= 1
        return ans
