class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        char_map = {"]":"[", "}":"{", ")":"("}
        for c in s:
            if stack and c in char_map and stack[-1] != char_map[c]:
                return False
            elif stack and c in char_map and stack[-1] == char_map[c]:
                stack.pop()
            else:
                stack.append(c)
        
        return not stack