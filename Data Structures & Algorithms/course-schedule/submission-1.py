class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = [[] for _ in range(numCourses)]
        indeg = [0] * numCourses
        for a, b in prerequisites:
            adj[b].append(a)
            indeg[a] += 1
        
        q = deque()
        for i in range(len(indeg)):
            if indeg[i] == 0:
                q.append(i)

        while q:
            v = q.popleft()

            for u in adj[v]:
                indeg[u] -= 1
                if not indeg[u]:
                    q.append(u)

        for x in indeg:
            if x != 0:
                return False
        return True 
        

