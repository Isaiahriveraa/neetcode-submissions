class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # We can use a hashmap for the void
        # 
        void = {}

        for i,n in enumerate(nums):
            if n in void:
                return [void[n], i]
            void[target - n] = i
    
        return []
            
