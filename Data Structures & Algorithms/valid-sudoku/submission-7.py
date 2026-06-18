class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """
        Given a 9 by 9 board
        each sub box can be calculated by r // 3 and c // 3
        we could use a set to do lookups
        [[".",".","4",".",".",".","6","3","."],
        [".",".",".",".",".",".",".",".","."],
        ["5",".",".",".",".",".",".","9","."],
        [".",".",".","5","6",".",".",".","."],
        ["4",".","3",".",".",".",".",".","1"],
        [".",".",".","7",".",".",".",".","."],
        [".",".",".","5",".",".",".",".","."],
        [".",".",".",".",".",".",".",".","."],
        [".",".",".",".",".",".",".",".","."]]
        """

        n = len(board)
        seen = defaultdict(set)

        for r in range(n):
            for c in range(n):
                cur = board[r][c]
                if cur == '.':
                    continue

                box = f"box{r//3}{c//3}"
                col = f"col{c}"
                row = f"row{r}"
                
                if cur in seen[box] or cur in seen[col] or cur in seen[row]:
                    return False
                    
                seen[box].add(cur)
                seen[col].add(cur)
                seen[row].add(cur)
        
        return True