class Solution:
    def minOperations(self, s: str) -> int:
        """
        Given a string that contains only 0's and 1's meanig that I can change the 0 and 1 

        The string is alternating if not two adj are equal 
        return  the min number of ops needed to make s alternating
        """   

        alt = '0'
        if s[0] == '1':
            alt = '1'
        
        res = 0

        # if we start with 0
        # if we start with 1 

        for i in range(1, len(s)):
            if i % 2 == 0 and s[i] != alt:
                res += 1
            elif i % 2 == 1 and s[i] == alt:
                res += 1
        
        return min(res, len(s) - res)