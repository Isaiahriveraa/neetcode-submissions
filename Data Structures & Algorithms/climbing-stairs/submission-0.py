class Solution:
    def climbStairs(self, n: int) -> int:
        
        # number of unique ways to climb the top of the star case
        memo = {}
        def dfs(n):
            if n == 0:
                return 1
            if n < 0:
                return 0
            
            if n in memo:
                return memo[n]
            
            one_step = dfs(n - 1)
            two_step = dfs(n - 2)

            memo[n] = one_step + two_step
            return memo[n]
        
        return dfs(n)
