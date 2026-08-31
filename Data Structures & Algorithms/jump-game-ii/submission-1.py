class Solution:
    def jump(self, nums: List[int]) -> int:
        
        """
        nums[i] reps the max lenght of a jump towards from index 

        i + cur index

        starting pos is at nums[0]

        return the min number of jumps to reach the last pos of in the array

        Greedy

        max? min?

        [2, 4, 1, 1, 1, 1]

         ^  ^  ^
        """

        dp = [-1] * len(nums) # index and the jumps

        def dfs(i):

            if i >= len(nums) - 1:
                return 0
                
            if dp[i] != -1:
                return dp[i]

            
            res = float('inf')
            
            if nums[i] == 0:
                return 100000

            for j in range(1, nums[i] + 1): # we can go up to the amt of nums[i]

                res = min(res, 1 + dfs(i + j))

            dp[i] = res
            
            return dp[i]
        
        return dfs(0)
                







        
        
