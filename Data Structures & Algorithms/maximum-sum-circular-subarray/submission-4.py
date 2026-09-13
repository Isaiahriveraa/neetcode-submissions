class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        
        glob_max = glob_min = nums[0]
        cur_max = cur_min = total = 0

        for n in nums:

            cur_max = max(n, cur_max + n)
            cur_min = min(n, cur_min + n)
            
            total += n

            glob_max = max(glob_max, cur_max)
            glob_min = min(glob_min, cur_min)
        
        return max(glob_max, total - glob_min) if glob_max > 0 else glob_max
            

