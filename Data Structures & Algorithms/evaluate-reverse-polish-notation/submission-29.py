class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        """
        1,2 + = 3
        If we get operator that means that we want to get the 2 prev numbers that way we can do a operation

        3, 3 * = 

        9, 4 - = 9 - 4 = 5

        For the - and / operators we want to use the 2nd pop from the stack to do the operation
        """

        stack = []

        for c in tokens:

            if c == '+':
                stack.append(stack.pop() + stack.pop())
            elif c == '*':
                stack.append(stack.pop() * stack.pop())
            elif c == '-':
                a, b = stack.pop(), stack.pop()
                stack.append(b - a)
            elif c == '/':
                a, b = stack.pop(), stack.pop()
                stack.append(int(b / a))
            else:
                stack.append(int(c))
        
        return stack[-1]