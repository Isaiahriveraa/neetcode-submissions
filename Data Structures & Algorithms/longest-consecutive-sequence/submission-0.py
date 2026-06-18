class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        We need to keep track 
        goal is to return the len of the longest conseq secq of E's that can be formed
        the seq must be 1 greater than the prev
        The elements do not have to be contigious in the original array
        Algo must be O(n)

        seen = 2
        seen = 20

        """
        if not nums:
            return 0
        
        seen = set()
        streak = 0

        for n in nums: 
            seen.add(n)
            start = n
            while start - 1 in seen: # that means there is nothing lower
                start -= 1
                
            cur_streak = 0
            while (start in seen):
                cur_streak += 1  
                start += 1
            streak = max(cur_streak, streak)
        
        return streak
                        

            
