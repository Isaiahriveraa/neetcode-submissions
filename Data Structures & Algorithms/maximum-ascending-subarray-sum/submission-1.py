class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        
        """
        Given an array of positive ints nums
        return the max possible sum of an strictly increaing subarry in nums
        """

        max_sum = 0
        l = 0
        cur_sum = 0

        for r, n in enumerate(nums):
            """
            nums=[12,17,15,13,10,11,12]
                  0   1  2  3
            12, 17, 15
            """
            # if the prev is greater than the  current we must remove from the left
            if r - 1 >= 0 and nums[r] <= nums[r - 1]:
                distance = r - l
                for _ in range(distance):
                    cur_sum -= nums[l]
                    l += 1
                
                
                
            cur_sum += n
            max_sum = max(cur_sum, max_sum)
        
        return max_sum