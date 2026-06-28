class Solution:
    def climbStairs(self, n: int) -> int:
        
        if n <= 1:
            return 1
        # number of unique ways to climb the top of the star case
        prev_one = 1
        prev_two = 1

        for i in range(2, n + 1):
            new = prev_one + prev_two
            prev_one = prev_two
            prev_two = new
        
        return prev_two