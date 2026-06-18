class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        goal: find the longest substring without duplicates

        algo's:
        - sliding window

        zxy res = 3
        then xyz = 3
        zxy = 3
        xyz = 3

        return 
        """
        l = 0
        res = 0
        seen = {}
        for r, c in enumerate(s):
            # if we have come across a duplicate character
            # but also the character is also in the current window
            # make the left pointer + 1 the last time we seen it that way we have no dupes
            if c in seen and seen[c] >= l:
                l = seen[c] + 1
            seen[c] = r
            res = max(res, r - l + 1)
    
        return res