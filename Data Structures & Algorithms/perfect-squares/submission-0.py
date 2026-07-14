class Solution:
    def numSquares(self, n: int) -> int:
        
        dp = {0: 0}

        for cur in range(1, n + 1):

            dp[cur] = float('inf')

            for i in range(1, cur + 1): # include cur so we do + 1
                sq = i ** 2

                if sq > cur: # sq is greater than what we need to find the min squares needed for cur num
                    break
                
                dp[cur] = min(dp[cur], 1 + dp[cur - sq])
            
        return dp[n]


        