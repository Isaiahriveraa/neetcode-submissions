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
        dp = [1] * (n) # have extra border for padding that
        # way we can avoid going out of bounds.
        for r in range(m - 1):
            for c in range(1, n):
                dp[c] += dp[c - 1]
        
        return dp[n - 1]
        # Tc: O(n * m)
        # SC: O(n)



