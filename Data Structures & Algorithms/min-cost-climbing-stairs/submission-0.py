class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        memo = {}
        def dfs(amt, i):
            if i >= len(cost):
                return amt
            
            if (amt, i) in memo:
                return memo[(amt, i)]
            
            one_step = dfs(amt + cost[i], i + 1)
            two_step = dfs(amt + cost[i], i + 2)
            
            memo[(amt, i)] = min(one_step, two_step)
            return memo[(amt, i)]
        return min(dfs(0, 1), dfs(0, 0))
        