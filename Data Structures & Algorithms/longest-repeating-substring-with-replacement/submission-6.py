class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        Given a string containing only uppercase characters

        we are given integer k

        we are trying to make the longest string of with duplicates

        xyyx, k = 2


        """
        max_len = 0
        l = 0
        char_count = defaultdict(int)
        max_freq = 0
        for r, c in enumerate(s):
            # if window - cur char count gives us the amt 
            # of characters that are not the current character
            # if we go above that means that we need to remove a character
            char_count[c] += 1
            max_freq = max(max_freq, char_count[c])
            while ((r - l + 1) - max_freq > k): # if the window is less than or equal to k
                char_count[s[l]] -= 1 #shrink the window but take off the left most character then increment
                l += 1
            max_len = max(r - l + 1, max_len)
        return max_len
