class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        
        # given nums
        # and k
        # choose an index
        # and increment the index by 1
        # return the max possible freq of an element after performing at most k opertations
        """
        1, 4, 8, 13

        k = 5

        we can only increase a number and we are trying to maxmize seeing a number

        keep track of also how much k's we have used
        """ 

        # brute force

        # trying to find a number that we can build to 
        # keep track of how many nums are less than this
        nums.sort() # that way we can make sure that we are updating the numbers on the left to try to get them to match the value
        res = 1
        for r in range(len(nums) - 1, -1, -1): # iterating in reverse
            cur_num = nums[r]
            l = r - 1
            spending = k
            while l >= 0 and spending > 0:
                # try to get the number equal to cur_num
                if nums[r] - nums[l] <= spending:
                    spending -= (nums[r] - nums[l])
                    res = max(r - l + 1, res)
                    l -= 1
                else:
                    break
    
        
        return res
                
                

            
