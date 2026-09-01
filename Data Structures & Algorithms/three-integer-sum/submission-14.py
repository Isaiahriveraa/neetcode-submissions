class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        res = []

        for i, num in enumerate(nums):

            if num > 0: # there is no possible triple going foward
                break

            if i > 0 and num == nums[i - 1]:
                continue
            
            l, r = i + 1, len(nums) - 1

            while l < r:

                target = num + nums[l] + nums[r] # triplet sum
            
                if target < 0:
                    l += 1
                elif target > 0: # adding to the sum
                    r -= 1
                else: # decrementing the sum
                    res.append([num, nums[l], nums[r]])

                    # used the numbers -> move them
                    l += 1
                    r -= 1

                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
            
        return res
