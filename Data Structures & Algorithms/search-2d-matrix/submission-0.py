
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        l = 0
        r = len(matrix)-1
        best = 0
        while(l <= r):
            k = (l + r) // 2

            if matrix[k][0] == target:
                return True
            if matrix[k][0] < target: 
                best = k
                l = k + 1
            else: 
                r = k - 1
        l = 0
        r = len(matrix[0])-1
        while(l <= r):
            k = (l + r) // 2

            if matrix[best][k] == target:
                return True
            if matrix[best][k] < target:
                l = k + 1
            else: r = r - 1
        
        return False

