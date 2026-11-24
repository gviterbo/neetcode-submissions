class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        directions = [[1,0], [-1,0], [0,1], [0,-1]]
        q = deque()
        fresh = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    q.append((i, j))
                elif grid[i][j] == 1:
                    fresh += 1
        ans = 0
        while q and fresh:
            ans += 1
            for _ in range(len(q)):
                r, c = q.popleft()
                for x, y in directions:
                    rw, cl = r+x, c+y
                    if 0 <= rw < n and 0 <= cl < m and grid[rw][cl] == 1:
                        q.append((rw, cl))
                        grid[rw][cl] = 2
                        fresh -= 1
        if not fresh:
            return ans
        return -1
                