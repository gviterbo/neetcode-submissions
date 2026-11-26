class DSU:
    def __init__(self, n):
        self.p = list(range(n))
        self.r = [0]*n

    def find(self, x) -> int:
        while x != self.p[x]:
            x = self.p[x]
        return x

    def unite(self, a, b) -> bool:
        a, b = self.find(a), self.find(b)
        if a == b: return False
        if self.r[a] > self.r[b]:
            a, b = b, a
        self.p[a] = b
        if self.r[a] == self.r[b]:
            self.r[b] += 1
        return True

class Solution:

    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        d = DSU(len(edges)+1)

        for a, b in edges:
            ans = d.unite(a, b)
            if not ans:
                return [a,b]