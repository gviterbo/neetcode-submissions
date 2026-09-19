class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        ans = [0]*(amount+1)

        for s in range(1, amount+1):
            ans[s] = float('inf')
            for c in coins:
                if s-c < 0:
                    continue
                if ans[s-c] == -1:
                    continue
                ans[s] = min(ans[s-c]+1, ans[s])
            if ans[s] == float('inf'):
                ans[s] = -1
        if ans[amount] == 0: 
            return -1
        return ans[amount]
        