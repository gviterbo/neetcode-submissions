class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        temp = [0] * 11
        for i in range(9):
            temp = [0] * 11
            for j in range(9):
                if board[i][j] == '.': 
                    continue
                else:
                    temp[int(board[i][j])] += 1

            for x in temp:
                if x >= 2: 
                    return False
        
        temp = [0] * 11
        for i in range(9):
            temp = [0] * 11
            for j in range(9):
                if board[j][i] == '.': 
                    continue
                else: 
                    temp[int(board[j][i])] += 1

            for x in temp:
                if x >= 2: 
                    return False
        
        temp = [0] * 11
        for i in range(3):
            for j in range(3):
                temp = [0] * 11
                for x in range(3):
                    for y in range(3):
                        if board[3*i+x][3*j+y] == '.':
                            continue 
                        k = int(board[3*i+x][3*j+y])
                        temp[k] += 1

                for x in temp:
                    if x >= 2:
                        return False


        return True