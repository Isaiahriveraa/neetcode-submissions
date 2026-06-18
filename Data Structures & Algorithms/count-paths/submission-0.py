class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        """
        Can either move right or down in one point in time it seems that we are repeating ourselves 
        meaning that we can try to calculate and drag our answer down

        dp approach that way we solve this in subproblems and drag those subproblems into the bottom
        right of our goal

        The contraint is small
        we are repeating work
        """
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)] # have extra border for padding that
        # way we can avoid going out of bounds.
        dp[0][1] = 1
        for r in range(m):
            for c in range(n):
                dp[r + 1][c + 1] = dp[r + 1][c] + dp[r][c + 1]
        
        return dp[m][n]

