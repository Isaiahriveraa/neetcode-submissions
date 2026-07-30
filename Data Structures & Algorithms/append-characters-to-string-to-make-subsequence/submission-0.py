class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        
        i = j = 0

        while i < len(s) and j < len(t):
            
            
            if s[i] == t[j]:
                # we have to move both
                i += 1
                j += 1
            else:
                i += 1

        return len(t) - j