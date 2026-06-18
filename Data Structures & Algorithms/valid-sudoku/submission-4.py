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
        rows = defaultdict(set)
        cols = defaultdict(set)
        seen = defaultdict(set)

        for r in range(n):
            for c in range(n):
                cur = board[r][c]
                if cur == '.':
                    continue
                cur_box = seen[(r // 3, c // 3)]
                if cur in cur_box or cur in rows[r] or cur in cols[c]:
                    return False
                    
                seen[(r // 3, c // 3)].add(cur)
                rows[r].add(cur)
                cols[c].add(cur)
        
        return True