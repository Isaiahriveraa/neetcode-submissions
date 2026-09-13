class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = cur_sum = max_sum = nums[0]
            
        for i in range(1, len(nums)):

            cur = nums[i]

            if cur_sum < 0: # restart
                cur_sum = 0
            
            cur_sum += cur
            max_sum += cur
            res = max(res, cur_sum, max_sum)
        
        return res