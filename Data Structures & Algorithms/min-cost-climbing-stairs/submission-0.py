class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        ans = [0]*len(cost)

        for i in range(2, len(cost)):
            ans[i] = min(ans[i-1] + cost[i-1], ans[i-2] + cost[i-2])
        
        n = len(cost)-1
        return min(ans[n]+cost[n], ans[n-1]+cost[n-1])

        