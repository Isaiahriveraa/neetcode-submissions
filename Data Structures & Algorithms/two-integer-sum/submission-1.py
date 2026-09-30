class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        """
        @problem
        nums = [3, 4, 5, 6] target = 7

        output: [0, 1]

        @given List[int]

        @return -> List[int]

        @optimize
        - Look up time -> hashmap
        - index -> hashmap we can tie indexes

        @example

        nums = [3, 4, 5, 6] target = 7
                ^ 
        calculation = target - nums[i] (store the number that we want to have that way we can match these 2 indexes to reach target)

        
        @algo
        iterate through num
        store the needed number to complete the two pair to equal the sum
        {need_this_number: index_of_other_num_to_reach_target}
        if the current number == need_this_number:
            return [hashmap[need_this_number], current_index]
        
        @contraints
        - cant use the same index
        - there will always be a pair that satifies the condition that we will fine a nums[i] + nums[j] == target
        - 2 <= nums.length <= 1000
        - -10,000,000 <= nums[i] <= 10,000,000
        - -10,000,000 <= target <= 10,000,000
        """

        lookup = {} # need_this_number: index
        for index, cur_number in enumerate(nums):

            # if we found the needed number to reach the target sum
            if cur_number in lookup:
                return [lookup[cur_number], index]
            
            # store the need_this_number
            lookup[target - cur_number] = index
        
        return [-1, -1]
