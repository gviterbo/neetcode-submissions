class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        adj = [[] for _ in range(len(edges)+1)]
        indeg = [0 for _ in range(len(edges)+1)]

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            indeg[v] += 1
            indeg[u] += 1

        q = deque()
        for i in range(len(indeg)):
            if indeg[i] == 1:
                indeg[i] -= 1
                q.append(i)

        while q: 
            u = q.popleft()
            for v in adj[u]:
                if indeg[v] == 0: continue
                indeg[v] -= 1
                if indeg[v] == 1:
                    indeg[v] -= 1
                    q.append(v)
        print(indeg)
        sol = set()
        for i in range(1,len(indeg)):
            ans = []
            if indeg[i] != 0:
                ans.append(i)
                for v in adj[i]:
                    if indeg[v] != 0:
                        ans.append(v)
                        sol.add((min(i,v), max(i,v)))
        for x, y in reversed(edges):
            if (x, y) in sol:
                return [x,y]