class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        
        n = len(grid)
        m = len(grid[0])

        for r in range(n):
            for c in range(m):
                if (r == 0 and c == 0):
                    continue
                # Goal is to figure out which nei to add to the current 
                # so look at the look up and look left
                cur_num = grid[r][c]
                top_nei = grid[r - 1][c] if r - 1 >= 0 else float('inf')
                left_nei = grid[r][c - 1] if c - 1 >= 0 else float('inf')
                
                grid[r][c] = min(cur_num + top_nei, cur_num + left_nei)
               
        
        return grid[n - 1][m - 1]


