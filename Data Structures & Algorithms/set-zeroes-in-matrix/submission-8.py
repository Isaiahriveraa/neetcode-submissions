class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        
        LAST_ROW = len(matrix) - 1
        LAST_COL = len(matrix[0]) - 1 

        # mark the last rows and the last cols 
        # that way when we traverse again we can
        # convert the cols and rows to zero if needed
        right_border = False
        bottom_border = False

        for r in range(len(matrix)): # right border traversal
            if matrix[r][LAST_COL] == 0:
                right_border = True

        for c in range(len(matrix[0])): # right border traversal
            if matrix[LAST_ROW][c] == 0:
                bottom_border = True

        for r in range(LAST_ROW):
            for c in range(LAST_COL):
                if matrix[r][c] == 0:
                    matrix[LAST_ROW][c] = float('inf')
                    matrix[r][LAST_COL] = float('inf')
        
        def row_zero(r):
            for c in range(len(matrix[0])):
                matrix[r][c] = 0

        def col_zero(c):
            for r in range(len(matrix)):
                matrix[r][c] = 0

        # make the row and the col zero
        for r in range(LAST_ROW):
            if matrix[r][LAST_COL] == float('inf') or matrix[r][LAST_COL] == 0:
                row_zero(r)
            
        for c in range(LAST_COL):
            if matrix[LAST_ROW][c] == float('inf') or matrix[LAST_ROW][c] == 0:
                col_zero(c)
        
        if right_border:
            col_zero(LAST_COL)
        
        if bottom_border:
            row_zero(LAST_ROW)

        
        


