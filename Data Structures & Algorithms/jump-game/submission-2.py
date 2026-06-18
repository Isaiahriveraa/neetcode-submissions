class Solution:
    def canJump(self, nums: List[int]) -> bool:
        memo = [-1] * len(nums)

        def dfs(i):
            if i == len(nums) - 1:
                return True

            if i >= len(nums):
                return False

            if memo[i] != -1:
                return False
            
            step = nums[i]
            for j in range(i + step, i, -1):
                if dfs(j):
                    return True
            memo[i] = 0
            return False
        return dfs(0)  