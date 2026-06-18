class MinStack:
    """
    So currently I'm trying to design a class that supports push, pop, pop, git min. 
    So push, pop, pop. I can order this within a movie in Python because it acts as a stack. 
    The git min I would have to optimize for because I don't want to search through the whole
    array to look for the minimum all the time. The way I would go about this is I would keep
    track of the minimum when I inserted these elements, right? What if we looked at the top, 
    right? If we looked at the top, then that means whatever it has for that element, it would
    be considered the minimum. I would use a tuple or a tuple and what that would mean is I 
    would push the element and then also push the current minimum. That way I can look at it 
    in constant time. See the end of the list, which is constant. Assuming there's no resizing 
    involved. Popping should be constant because it'll work as a stack, right? And then the 
    top will look at the top of the list with a stack in Python. It's built in the right. 
    And then we'll just look at the first index instead of the 0th index. for the top.
    """

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append((val, val))
        else:
            cur_min = min(val, self.stack[-1][1])
            self.stack.append((val, cur_min))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]
