from collections import deque
class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        l = 0
        w = 0
        n, m = len(grid), len(grid[0])
        for x in grid:
            for y in x: 
                if y == 1: l = 1
                if y == 0: w = 1
        if (l and not w) or (w and not l):
            return -1

        directions = [[1,0], [-1,0], [0,-1], [0,1]]

        q = deque()
        dist = [[0 for _ in range(m)] for _ in range(n)]
        fresh = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    q.append((i,j))
                if grid[i][j] == 0:
                    fresh += 1
        d = 0
        ans = 0
        while q and fresh:
            d += 1
            ans = max(d, ans)
            for _ in range(len(q)):
                r, c = q.popleft()
                for dx, dy in directions:
                    nx, ny = r+dx, c+dy
                    if 0<= nx<n and 0 <=ny<m and grid[nx][ny] == 0:
                        grid[nx][ny] = 1
                        dist[nx][ny] = d
                        q.append((nx, ny))
                        fresh -= 1
        
        return ans
