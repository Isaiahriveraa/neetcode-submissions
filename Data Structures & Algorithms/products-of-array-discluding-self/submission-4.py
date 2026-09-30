class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
    
        """
        @given int array nums
        @return List[int]
    
        @goal
        - implement a way for us to return a resulting array
            - the array must be product of eveything in the array but itself
    
        @walkthrough
        - nums = [1, 2, 3, 4]
        - visually the calculation for it looks like this
        - [[2 * 3 * 4], [1 * 3 * 4], [1 * 2 * 4], [1 * 2 * 3]]
        - Turns into this
        - [24, 12, 8, 6]
    
        @algorithm & rationale
        - prefix + suffix
        - that way for an ith element we can check the product on everything but itself on the left
        - everything on the right of it
    
        N = len(nums) "we visit each element once"
    
        @time complexity
        - O(2 * N) -> O(N)
    
        @space complexity
        - O(N)
        """
        res = []
        pre_array = []
        prefix_prod = 1
        for i in range(len(nums)):
            pre_array.append(prefix_prod)
            prefix_prod *= nums[i]
    
        suf_array = []
        suffix_prod = 1
        for i in range(len(nums) - 1, -1, -1):
            suf_array.append(suffix_prod)
            suffix_prod *= nums[i]
    
        for i in range(len(nums)):
            # at this ith index whats the prod to the left and the right
            product_to_left = pre_array[i]
            product_to_right = suf_array[len(nums) - 1 - i]
            product_but_itself = product_to_left * product_to_right
            res.append(product_but_itself)
    
        return res
 