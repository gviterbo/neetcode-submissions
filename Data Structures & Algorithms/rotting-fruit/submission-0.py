class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        directions = [[1,0], [-1,0], [0,1], [0,-1]]
        
        n, m = len(grid), len(grid[0])
        
        def padding(grid) -> List[List[int]]:
            mtx = [[0 for _ in range(m+2)] for _ in range(n+2)]

            for i in range(1, n+1):
                for j in range(1, m+1):
                    mtx[i][j] = grid[i-1][j-1]
            return mtx
        
        mtx = padding(grid)

        ans = [[100 for _ in range(m)] for _ in range(n)]

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0 or grid[i][j] == 2:
                    ans[i][j] = 0
        def bfs(i, j, mtx):
            q = deque()
            mtx[i][j] = 0
            q.append((i,j,0))
            ans[i-1][j-1] = 0
            while q:
                r, c, t = q.popleft()
                for x, y in directions:
                    linha = r+x
                    coluna = y+c
                    if mtx[linha][coluna] == 1:
                        q.append((linha, coluna, t+1))
                        mtx[linha][coluna] = 0
                        ans[linha-1][coluna-1] = min(t+1,ans[linha-1][coluna-1])

        for i in range(1,n+1):
            for j in range(1, m+1):
                if mtx[i][j] == 2:
                    temp = [row[:] for row in mtx]
                    bfs(i, j, temp)
        res = 0
        for i in range(n):
            for j in range(m):
                res = max(res, ans[i][j])
        
        if res == 100:
            return -1
        return res




















        