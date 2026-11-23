class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        def transpose(matrix):
            for i in range(n):
                for j in range(i, n):
                    matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        transpose(matrix)

        for row in matrix:
            row.reverse()
        
        