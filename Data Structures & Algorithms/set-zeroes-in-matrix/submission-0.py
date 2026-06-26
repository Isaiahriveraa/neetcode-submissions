class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        row = set()
        col = set()

        m, n = len(matrix), len(matrix[0])

        for r in range(m):
            for c in range(n):
                if matrix[r][c] == 0:
                    row.add(r)
                    col.add(c)
        
        for r in row:
            for c in range(n):
                matrix[r][c] = 0
        
        for c in col:
            for r in range(m):
                matrix[r][c] = 0
        
        
        