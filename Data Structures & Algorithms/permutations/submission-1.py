class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        

        used = [False] * len(nums)
        res = []

        """
        @behavior find all unique permutations by 
        """
        def dfs(i, subset):
            if i == len(nums):
                res.append(subset.copy())
                return 

            if i >= len(nums): # bounds check
                return

            for j in range(len(nums)):
                if used[j]:
                    continue
                # else index isnt used in the current permutation
                subset.append(nums[j])
                used[j] = True
                dfs(i + 1, subset) # this is keeping track of how many numbers we have in the permutation
                subset.pop()
                used[j] = False

            return

        dfs(0, [])

        return res
            

            
            
