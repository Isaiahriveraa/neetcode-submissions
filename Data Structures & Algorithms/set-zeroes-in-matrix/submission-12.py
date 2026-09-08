class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        
        LAST_ROW = len(matrix) - 1
        LAST_COL = len(matrix[0]) - 1
    
        # Check the bottom border or the right border if there are 0's there 
        bottom = False
        right = False

        for r in range(LAST_ROW + 1): # consider the corner itself
            if matrix[r][LAST_COL] == 0:
                right = True

        for c in range(LAST_COL + 1):
            if matrix[LAST_ROW][c] == 0:
                bottom = True

        # Now we want to consider the matrix that is not on the bottom border or the right border
        # We can refer to this is an the inner cases 
        # if we find a 0: 
        #    mark the end of the col and the row as float('inf')
            
        for r in range(LAST_ROW):
            for c in range(LAST_COL):
                if matrix[r][c] == 0:
                    matrix[r][LAST_COL] = 0
                    matrix[LAST_ROW][c] = 0
        
        def make_row_zero(r):
            for c in range(len(matrix[0])):
                matrix[r][c] = 0
                
        def make_col_zero(c):
            for r in range(len(matrix)):
                matrix[r][c] = 0

        for r in range(LAST_ROW):
            if matrix[r][LAST_COL] == 0:
                # make the row zero
                make_row_zero(r)
        
        for c in range(LAST_COL):
            if matrix[LAST_ROW][c] == 0:
                # make the col zero
                make_col_zero(c)
        
        if right:
            make_col_zero(LAST_COL)
        
        if bottom:
            make_row_zero(LAST_ROW)
        