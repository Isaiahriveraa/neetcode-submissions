class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        ROWS, COLS = len(obstacleGrid), len(obstacleGrid[0])
        memo = [[-1]*COLS for _ in range(ROWS)] # start with -1 that way we can say that this path has not been traversed

        def dfs(r, c):
            if obstacleGrid[r][c] == 1: # we hit obstacle
                return 0

            if r == ROWS - 1 and c == COLS - 1:
                return 1 # we reached the bottom right
            
            if memo[r][c] != -1:
                return memo[r][c]
            
            down = 0 
            right = 0

            if r + 1 < ROWS:
                down = dfs(r + 1, c)
            if c + 1 < COLS:
                right = dfs(r, c + 1)
            
            memo[r][c] = down + right
            return memo[r][c]

            
        return dfs(0, 0)