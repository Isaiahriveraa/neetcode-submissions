class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        target = sum(nums) 
        if target % 2 == 1:
            return False

        target //= 2
        
        # what matters is here is finding a sum that is == half of the whole sum of nums

        cache = {}

        def dfs(total, i, target):

            if total == target:
                return True
            
            if i >= len(nums):
                return False
            
            if total > target:
                return False
            
            if (total, i) in cache:
                return cache[(total, i)]
            
            include = dfs(total + nums[i], i + 1, target)
            dont_include = dfs(total, i + 1, target)
            
            cache[(total, i)] = include or dont_include

            return cache[(total, i)]
                
    

        return dfs(0, 0, target)
             