class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        # given nums in sorted order
        # find the starting and ending pos of the target value

        # make a binary search that finds the target first time
        def find_first_instance(target):

            n = len(nums)
            l, r = 0, n
            
            while l < r:
                
                mid = (l + r) // 2
                # trying to go left as possible

                if nums[mid] >= target:
                    # go left window
                    r = mid
                else: # go to the right window
                    l = mid + 1
            
            # we found the index 
            return l # we can also return nums[r]

        
        start_index = find_first_instance(target)
        end_index = find_first_instance(target + 1) - 1
    
        return [start_index, end_index] if (start_index < len(nums) and nums[start_index] == target) else [-1,-1]

 