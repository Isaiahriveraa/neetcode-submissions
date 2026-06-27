class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        

        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        paths = [[0] * n for _ in range(m)]

        # can only go right and bottom that means that the col can only go r + 1 and c + 1
        # return the number of unique paths, so we can do top down approach or the bottom up approach
        # the bottom up approach makes you think what are the possible paths from the nei pos
        # that means bring the ans down look at ur nei and add it to yourself
        if obstacleGrid[0][0] == 1:
            return 0
        
        paths[0][0] = 1 # a robot path can come from here

        for r in range(m):
            for c in range(n):
                if r == 0 and c == 0:
                    continue
                
                if obstacleGrid[r][c] == 1:
                    continue
                
                if r - 1 >= 0:
                    paths[r][c] += (paths[r - 1][c])    
                if c - 1 >= 0:
                    paths[r][c] += (paths[r][c - 1])    
                

        return paths[m - 1][n - 1]

            