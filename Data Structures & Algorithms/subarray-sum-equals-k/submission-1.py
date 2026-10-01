class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        """
        @given
        - nums: List[int]
        - k: int

        @return the total number of subarrays that sum equlas to k

        @walkthrough
        nums = [2, -1, 1, 2] | k = 2
    
        @algos
        - prefix and suffix (we keep track of how many subrrays on the left equal k adn the right)    
        """
        seen = {0: 1}

        res = 0
        prefix_sum = 0

        for num in nums:
            prefix_sum += num
            prev_prefix_sum = prefix_sum - k
            res += seen.get(prev_prefix_sum, 0)
            seen[prefix_sum] = 1 + seen.get(prefix_sum, 0)
        
        return res