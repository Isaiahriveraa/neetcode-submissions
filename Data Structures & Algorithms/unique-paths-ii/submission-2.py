class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        ROWS, COLS = len(obstacleGrid), len(obstacleGrid[0])

        dp = [[0] * COLS for _ in range(ROWS)]

        if obstacleGrid[0][0] == 1: # meanning we cant start bc thats the obstancle blocking
            return 0

        dp[0][0] = 1 # that start is validated

        for r in range(ROWS):
            for c in range(COLS):
                # your logic here
                if obstacleGrid[r][c] == 1:
                    dp[r][c] = 0 # meaning that we cannot go here so there are 0 paths from here
                    continue

                if r > 0:
                    dp[r][c] += dp[r - 1][c] 

                if c > 0:
                    dp[r][c] += dp[r][c - 1] 

        return dp[ROWS - 1][COLS - 1]