class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        
        n = len(nums)
        used = [False] * n
        res = []
        subset = []
        nums.sort()
        
        def dfs():

            # if the len of the list == nums add it that means that we found a permutation
            if len(subset) == len(nums):
                res.append(subset.copy())
                return
            
            for i in range(len(nums)):
                if used[i]:
                    continue

                if i > 0 and nums[i] == nums[i - 1] and used[i - 1]:
                    continue

                subset.append(nums[i])
                used[i] = True
                dfs()
                subset.pop()
                used[i] = False
        
            return
        
        dfs()
        return res












