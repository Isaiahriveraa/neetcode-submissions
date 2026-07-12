class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        
        n = len(nums)
        l, r = 0, n - 1

        while l <= r:

            mid = (l + r) // 2

            # check the nei

            left_nei = nums[mid - 1] if mid - 1 >= 0 else float('inf')
            right_nei = nums[mid + 1] if mid + 1 < n else float('inf')

            if nums[mid] != left_nei and nums[mid] != right_nei:
                return nums[mid]
            elif nums[mid] == right_nei:
                # calculate the right window length
                start_of_right_window = mid + 2
                if (r - start_of_right_window + 1) % 2 == 1: # if the right window is odd go right 
                    l = start_of_right_window
                else:
                    r = mid - 1
            else: # mid == left nei

                end_of_left_window = mid - 2

                if (end_of_left_window - l + 1) % 2 == 1: # if the left window is odd
                    r = end_of_left_window
                else:
                    l = mid + 1
            
        return -1

