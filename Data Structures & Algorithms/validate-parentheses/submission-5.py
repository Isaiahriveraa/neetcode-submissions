class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []
        for char in s:
            if not stack:
                stack.append(char)
            elif stack:
                if char == ']' and stack[-1] == '[':
                    stack.pop()
                elif char == '}' and stack[-1] == '{':
                    stack.pop()
                elif char == ')' and stack[-1] == '(':
                    stack.pop()
                else:
                    stack.append(char)
        return not stack
            