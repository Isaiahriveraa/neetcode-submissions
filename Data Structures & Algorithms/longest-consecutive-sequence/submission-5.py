class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        list_nums = set(nums)

        res = 0
        for n in list_nums:
            length = 1

            while n + 1 in list_nums:
                length += 1
                n += 1

            res = max(res, length)
        
        return res
            
