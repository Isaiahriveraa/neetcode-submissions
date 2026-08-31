class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        rows, cols, sub_box = set(), set(), set()

        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == '.':
                    continue

                if ((r, board[r][c]) in rows or
                    (c, board[r][c]) in cols or
                    (board[r][c], r // 3, c // 3) in sub_box):

                    return False
                
                rows.add((r, board[r][c]))
                cols.add((c, board[r][c]))
                sub_box.add((board[r][c], r // 3, c // 3))
                
        return True
                    