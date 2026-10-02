class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []
        closing = { "}": "{", ")": "(", "]": "["}

        for char in s:
            if char in closing:
                if stack and closing[char] == stack[-1]:
                    stack.pop()
                else: # can't close a bracket
                    return False
            else: # if not stack or its an opening bracket
                stack.append(char)
            
        return not stack
            