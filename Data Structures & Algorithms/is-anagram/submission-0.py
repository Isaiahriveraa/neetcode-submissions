# from Collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        # same strings so they sort them and then compare naive
        # return sorted(s) == sorted(t)
        # map?
        res = 0
        char_map = defaultdict(int)

        for c in s:
            char_map[c] += 1

        res = 0

        for c in t:
            char_map[c] -= 1
            if char_map[c] + 1 == 0:
                res -= 1
            elif char_map[c] == 0:
                res += 0
        
        return res == 0

