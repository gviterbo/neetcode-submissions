class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n = len(grid)
        m = len(grid[0])

        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        def padding(grid) -> List[List[str]]:
            mtx = [["0" for _ in range(m + 2)] for _ in range(n + 2)]
            for i in range(1, n + 1):
                for j in range(1, m + 1):
                    mtx[i][j] = grid[i - 1][j - 1]
            return mtx

        mtx = padding(grid)

        def bfs(i, j):
            q = deque()
            mtx[i][j] = "0"
            q.append((i,j))

            while q:
                r, c = q.popleft()
                for x, y in directions:
                    if mtx[x+r][c+y] == "1":
                        q.append((x+r, c+y))
                        mtx[x+r][y+c] = "0"
        ans = 0
        for i in range(1, n+1):
            for j in range(1, m+1):
                if mtx[i][j] == "1":
                    bfs(i,j)
                    ans += 1
        return ans