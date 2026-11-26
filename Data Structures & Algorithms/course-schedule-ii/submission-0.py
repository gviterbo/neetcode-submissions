class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = [[] for _ in range(numCourses)]
        indeg = [0 for _ in range(numCourses)]
        for a,b in prerequisites:
            adj[b].append(a)
            indeg[a] += 1
        
        q = deque()
        ans = []

        for i in range(len(indeg)):
            if indeg[i] == 0:
                q.append(i)
        
        while q:
            v = q.popleft()
            ans.append(v)
            for u in adj[v]:
                indeg[u] -= 1
                if indeg[u] == 0:
                    q.append(u)

        if len(ans) < numCourses:
            return []
        return ans

