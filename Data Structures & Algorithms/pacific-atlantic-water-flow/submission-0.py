import copy
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        def padding(grid) -> List[List[str]]:
            mtx = [[0 for _ in range(len(heights[0]) + 2)] for _ in range(len(heights) + 2)]
            for i in range(1, len(heights) + 1):
                for j in range(1, len(heights[0]) + 1):
                    mtx[i][j] = grid[i - 1][j - 1]
            return mtx
        mtx = padding(heights)
        n, m = len(mtx), len(mtx[0])
        p_grid = copy.deepcopy(mtx)
        a_grid = copy.deepcopy(mtx)
        
        directions = [[1,0], [-1,0], [0,1], [0,-1]]
        vp = [[0 for _ in range(m)] for _ in range(n)]
        
        va = [[0 for _ in range(m)] for _ in range(n)]
        
        qp = deque()
        qa = deque()

        for j in range(m-1):
            a_grid[0][j] = -1
            vp[0][j] = 1
            qp.append((0,j))

        for i in range(1,n-1):
            a_grid[i][0] = -1
            vp[i][0] = 1
            qp.append((i,0))

        for j in range(m):
            p_grid[n-1][j] = -1
            va[n-1][j] = 1
            qa.append((n-1,j))

        for i in range(n-1):
            p_grid[i][m-1] = -1
            va[i][m-1] = 1
            qa.append((i, m-1))


        while(qp):
            for _ in range(len(qp)):
                r, c = qp.popleft()
                for x, y in directions:
                    dx, dy = r+x, c+y
                    if 0<=dx<n and 0<=dy<m and p_grid[r][c] <= p_grid[dx][dy] and vp[dx][dy] == 0:
                        vp[dx][dy] = 1
                        qp.append((dx,dy))
        while(qa):
            for _ in range(len(qa)):
                r, c = qa.popleft()
                for x, y in directions:
                    dx, dy = r+x, c+y
                    if 0<=dx<n and 0<=dy<m and a_grid[r][c] <= a_grid[dx][dy] and va[dx][dy] == 0:
                        va[dx][dy] = 1
                        qa.append((dx,dy))
        ans = []
        for i in range(n):
            for j in range(m):
                if vp[i][j] == 1 and va[i][j] == 1:
                    ans.append([i-1,j-1])
        
        return ans
        