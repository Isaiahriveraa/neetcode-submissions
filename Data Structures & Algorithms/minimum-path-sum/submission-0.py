class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        
        n = len(grid)
        m = len(grid[0])

        for r in range(n):
            for c in range(m):
                if r == 0 and c == 0:
                    continue
                # Goal is to figure out which nei to add to the current 
                # so look at the look up and look left

                if r - 1 >= 0 and c - 1 >= 0:
                    cur_num = grid[r][c]
                    grid[r][c] = min(cur_num + grid[r - 1][c], cur_num + grid[r][c - 1])
                
                if r - 1 >= 0 and c - 1 < 0: # that only the top nei can be checked
                    grid[r][c] += grid[r - 1][c]
                elif c - 1 >= 0 and r - 1 < 0:
                    grid[r][c] += grid[r][c - 1]
        
        return grid[n - 1][m - 1]


