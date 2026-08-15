class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        """
        What is a palindrome meaning that it is the same 
        """
        res = [-1, -1]
        length = 0
        for i in range(len(s)):
            # we need to handle both cases of odd and even
            l, r = i, i

            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l + 1 > length:
                    length = r - l + 1
                    res = [l, r + 1]
                l -= 1
                r += 1 
            
            l, r = i, i + 1

            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l + 1 > length:
                    length = r - l + 1
                    res = [l, r + 1]
                l -= 1
                r += 1 
                
        return s[res[0]: res[1]]