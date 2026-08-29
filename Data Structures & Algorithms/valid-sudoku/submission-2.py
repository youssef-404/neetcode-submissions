class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        col= set()
        row= set()
        block = set()
        for i in range(9):
            col.clear()
            row.clear()
            block.clear()
            bigJ = (i%3)*3
            bigI = (i//3)*3
            for j in range(9):
                if board[i][j]!= '.':
                    if board[i][j] in col:
                        return False
                    col.add(board[i][j])
                if board[j][i]!= '.':
                    if board[j][i] in row:
                        return False
                    row.add(board[j][i])
    
                smallJ = j%3
                smallI = j//3
                if board[bigI+smallI][bigJ+smallJ]!= '.':
                    if board[bigI+smallI][bigJ+smallJ] in block:
                        return False
                    block.add(board[bigI+smallI][bigJ+smallJ])
        
        return True
