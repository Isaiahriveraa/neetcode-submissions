class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        """
        @problem

            @given s: str and t: str
            @definitions
            anagrams -> if the string contains the same characters and the same frequency of them then str a and str b are the anagrams of each other.

        @return boolean (true or false)
            @condition 
            if the 2 strings are anagrams of each other:
                return TRUE
            else:
                continue to look for the res

        @optimize
        - only lowercase chars -> we can use 2 arrays [0] * 26 
            - that way we can represent them as 2 constant arrays -> O(1) for Space complexity
            - index of the array maps to a char (a - z)
            - use the ord('${char}') operation to calulate the char's numeric value in ascii
        @contraints
            - lowercase chars
            - 1 <= s.length, t.length <= 5 * 10 ** 4 
        """
        # can't be anagrams if they don't have the same str size
        if len(s) !=  len(t): 
            return False

        s_char_count = [0] * 26
        t_char_count = [0] * 26

        # iterate through s and t
        for i in range(len(t)):

            s_char_count[ord(s[i]) - ord('a')] += 1
            t_char_count[ord(t[i]) - ord('a')] += 1

        for i in range(26):
            if s_char_count[i] != t_char_count[i]:
                return False
        
        return True

