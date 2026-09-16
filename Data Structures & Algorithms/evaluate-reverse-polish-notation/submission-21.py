class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = []
        """
        tokens=["4","13","5","/","+"]

        4, 13, 5
        13 / 5 => 2
        2 + 4 = 6
        """

        for c in tokens:

            if c == '+':
                a, b = stack.pop(), stack.pop()
                stack.append(int(b) + int(a))
            elif c == '-':
                a, b = stack.pop(), stack.pop()
                stack.append(int(b) - int(a))
            elif c == '*':
                a, b = stack.pop(), stack.pop()
                stack.append(int(b) * int(a))
            elif c == '/':
                a, b = stack.pop(), stack.pop()
                stack.append(int(b) / int(a))
            else:
                stack.append(c)

        return int(stack[-1])