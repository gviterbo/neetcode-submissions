class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hm = {}
        for x in nums:
            hm[x] = hm.get(x, 0) + 1
        ans = []
        for x in hm.keys():
            ans.append([hm[x], x])
        ans.sort(reverse = True)
        ans2 = []
        for i in range(k):
            ans2.append(ans[i][1])
        return ans2
