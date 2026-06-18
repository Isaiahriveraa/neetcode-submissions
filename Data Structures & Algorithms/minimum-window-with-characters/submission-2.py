from collections import Counter
from collections import defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """
        I am given two string s & t we need to return the shorest substring of s

        meaning that every letter in t including dupes is present in the substring, if this substring
        does not exsit then i need to return a empty string


        s and t

        algo: sliding window
        we need to make sure that s contains t whats the min substring that contains t

        the way to optimize is to keep track of matches

        OUZODYXAZV T = XYZ

        O = 2
        U = 1
        Z = 1
        D = 1
        Y = 1 

        Y IN T_MAP AND IT MATCHES COUNT: MATCHES += 1
        MATCHES = 1
        Z IN T SO WE HAVE A MATCH

        """
        if len(s) < len(t):
            return ""

        t_map = Counter(t)
        s_map = defaultdict(int)
        l = 0
        matches = 0
        # res = startidx, endidx (need to do + 1 at the end exclusive)
        res = [0, 0, float('inf')]
        for r, c in enumerate(s):
            # increment the count of the char
            s_map[c] += 1
            # if the c in t map and the count is the same we have a match
            if c in t_map and t_map[c] == s_map[c]:
                matches += 1
            # if the matches all line up with t_map & the window > our cur window
            while matches == len(t_map):
                if r - l + 1 < res[2]:
                    res = [l, r, r - l + 1]
                # lets try to shrink the window now that we found the matches lets try to get rid
                # of as much as we can while losing one match
                #remove char
                s_map[s[l]] -= 1
                if s[l] in t_map and s_map[s[l]] < t_map[s[l]]:
                    matches -= 1
                l += 1

        l, r = res[0], res[1] + 1
        return s[l : r] if res[2] != float('inf') else ""