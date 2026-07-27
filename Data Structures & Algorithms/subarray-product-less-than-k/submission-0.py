class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0
            
        N = len(nums)
        l = 0
        res = 0
        product = 1

        for r in range(N):

            # include current num
            product *= nums[r]

            while product >= k:
                # remove the left
                product //= nums[l]
                l += 1

            res += (r - l + 1)
        
        return res