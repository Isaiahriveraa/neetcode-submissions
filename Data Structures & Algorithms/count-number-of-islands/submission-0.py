class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        # we can use dfs to figure out a island
        # mark it as visited making it a 0 meaning we dont visit it again

        def dfs(r, c):
            # in bounds check
            if (r < 0 or r >= len(grid) or
                c < 0 or c >= len(grid[0])):
                return

            # water case (not an island) or already visited
            if grid[r][c] == "0":
                return
            
            # mark as visited
            grid[r][c] = "0"

            dfs(r + 1, c) # down
            dfs(r - 1, c) # up
            dfs(r, c + 1) # right
            dfs(r, c - 1) # left

            return
    
        m, n = len(grid), len(grid[0])

        res = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] == "1": # enter and explore 
                # update res, and explore whole island and mark as visited
                    dfs(r, c)
                    res += 1
        return res
                