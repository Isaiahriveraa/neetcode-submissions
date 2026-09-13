class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        

        used = set()
        res = []

        """
        @behavior find all unique permutations by checking if the current index is used in the subset if it is skip it otherwise use this index
        once index is == len(subset) -> 
        """
        def dfs(i, subset):
            if i == len(nums):
                res.append(subset.copy())
                return 

            if i >= len(nums): # bounds check
                return

            for j in range(len(nums)):
                if j in used:
                    continue
                # else index isnt used in the current permutation
                subset.append(nums[j])
                used.add(j)
                dfs(i + 1, subset) # this is keeping track of how many numbers we have in the permutation
                subset.pop()
                used.remove(j)

            return


        dfs(0, [])
        return res

        """
        N = len(nums)

        time complexity:
        - N to copy the subset to res
        - N! choices we can go
        - O(N * N!)
        space complexity:
        - O(N) aux space
        - o (N * N!) output space 
        """

