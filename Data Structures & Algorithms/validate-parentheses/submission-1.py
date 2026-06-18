class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        char_map = {"]":"[", "}":"{", ")":"("}
        for c in s:
            if c in char_map:
                if stack and stack[-1] == char_map[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        
        return not stack