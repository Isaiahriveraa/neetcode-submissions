class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        Given char's that are only upper case characters to an int l 

        I am given k replacesments with any other character to make the longest string
        the string can only contain one character after k replacements.

        s = xyyx k = 2
        output = 4 because we can replace those two y's 

        There is an edge case we dont need a hashmap because we dont need to record the character with longest idk

        XYYX K = 2

        Using sliding window but we have to care 

        Lets just go with the hashmap approach what does that mean that means that we need to record the
        first time we seen this character and whats the longest substring we can make with it.

        AAABAAB

        A = 0
        AAA NOW WE HIT A B LETS GO WE HAVE K STILL A THEN THE NEXT IS B AND OUR K IS NOT > 0
        ohhh its number of a characer vs the window size and i
        while k > 0:    
        
        A = 3
        NOW WINDOW IS 4 AND 4 - 3 = 1 <= K





        a = 1
        a = 2
        a = 3
        B = 1
        4 - 3 = 1 <= k
        add another A 5 - 4 <= 1 

        """
        l = 0
        seen = defaultdict(int)
        res = 0
        max_c = [s[0], 1]
        for r, c in enumerate(s):
            seen[c] += 1
            # if the current c > the most common char we say
            if seen[c] > max_c[1]:
                max_c = [c, seen[c]]

            window = (r - l + 1)
            if window - max_c[1] <= k:
                res = max(res, window)
            else:
                seen[s[l]] -= 1
                l += 1
        
        return res
            
