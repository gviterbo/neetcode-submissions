class Solution:

    def rs(self, hm: dict) -> int:
        total = 0
        m = 0
        for x in hm.values():
            m = max(m, x)
            total += x
        return total - m

    def characterReplacement(self, s: str, k: int) -> int:
        hm = {}
        l = 0
        ans = 0

        for r in range(len(s)):
            hm[s[r]] = hm.get(s[r], 0) + 1
            while self.rs(hm) > k:
                hm[s[l]] -= 1
                l += 1
            ans = max(ans, r-l+1)
        return ans
            