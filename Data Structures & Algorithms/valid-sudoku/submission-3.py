class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen_row = set()
        seen_col = set()
        size = len(board[0])
    
        for ct in range(size):
            seen_col.clear()
            seen_row.clear()

            for row in range(size):
                if board[ct][row] != '.':
                    if board[ct][row] in seen_row:
                        return False
                    seen_row.add(board[ct][row])
                if board[row][ct] != '.':
                    if board[row][ct] in seen_col:
                        return False
                seen_col.add(board[row][ct])
    
        for i in range(size*3):
            x = i%9
            rest = i//9
            if i%3==0:
                seen_row.clear() 
            for j in range(3):
                y = rest*3 +j
                if board[x][y] != '.':
                    if board[x][y] in seen_row:
                        return False
                    seen_row.add(board[x][y])

        return True