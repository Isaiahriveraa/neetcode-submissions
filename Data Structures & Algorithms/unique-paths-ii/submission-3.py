class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        ROWS, COLS = len(obstacleGrid), len(obstacleGrid[0])

        if obstacleGrid[0][0] == 1: # meanning we cant start bc thats the obstancle blocking
            return 0

        obstacleGrid[0][0] = 1

        for r in range(ROWS):
            for c in range(COLS):
                if r == 0 and c == 0:
                    continue
            
                if obstacleGrid[r][c] == 1:
                    obstacleGrid[r][c] = 0 # meaning that we cannot go here so there are 0 paths from here
                    continue

                
                above = obstacleGrid[r - 1][c] if r > 0 else 0
                left = obstacleGrid[r][c - 1] if c > 0 else 0

                obstacleGrid[r][c] = above + left

        return obstacleGrid[ROWS - 1][COLS - 1]