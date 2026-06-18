class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Goal: Find the longest substr without dupes 
        add c
        if i get a dupe
            shrink the window until no dupes
        
        2 approaches:
            shrink until or i can say if i have this c in my window and 
            or i can see the last time i seen it and if its in my window
            make the start of my window + 1 from the last time we seen that character
        """
        res = 0
        last_seen = {}
        l = 0
        for r, c in enumerate(s):
            if c in last_seen and l <= last_seen[c]:
                l = last_seen[c] + 1
            last_seen[c] = r
            res = max(r - l + 1, res)
        return res
