class Solution:
    def rob(self, nums: List[int]) -> int:
        
        # given an int nums where 
        # the ith element represents the amt of money the ith house has
        # the houses are arrange in a straight line
        
        # planning to rob the money freom the houses but we cannot rob nei
        # if we robbed the current house 
        # return the max amt we can can rob without alerting the police
        
        # 1, 1, 3, 3
        # Choices that we have are 
    
        n = len(nums)
        memo = {}
        def dfs(i):

            # if we are out of bounds we must stop
            if i >= n:
                return 0

            if i in memo:
                return memo[i]
            
            rob = nums[i] + dfs(i + 2)
            dont_rob = dfs(i + 1)

            memo[i] = max(rob, dont_rob)

            return memo[i]

        return dfs(0)




            