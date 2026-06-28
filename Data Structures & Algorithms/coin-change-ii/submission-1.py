class Solution:
    def change(self, amt: int, coins: List[int]) -> int:
        memo = {}
        def dfs(i, remaining):
            if remaining < 0:
                return 0
            
            if remaining == 0:
                return 1
            
            if (i, remaining) in memo:
                return memo[(i, remaining)]
            
            if i >= len(coins):
                return 0
            
            use = dfs(i, remaining - coins[i])
            not_use = dfs(i + 1, remaining)


            memo[(i, remaining)] = use + not_use
            return memo[(i, remaining)]
    
        return dfs(0, amt)
     