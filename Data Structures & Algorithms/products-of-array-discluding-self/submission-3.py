class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        1, 2, 4, 8
       
        """ 
        pre_arr = []
        prefix = 1
        for n in nums:
            pre_arr.append(prefix)
            prefix *= n
        
        suffix = 1
        #modify the prefix array and return it iterate through the given nums
        #iterate in reverse
        for i in range(len(nums) -1, -1, -1):
            pre_arr[i] *= suffix
            print(nums[i])
            suffix *= nums[i]
        
        return pre_arr