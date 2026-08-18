class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        first, second = [0] * 26, [0] * 26 
        for c in s:
            first[ord(c) - ord('a')] += 1
        for c in t:
            second[ord(c) - ord('a')] += 1
        
        return first == second