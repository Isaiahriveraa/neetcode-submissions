class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append((val, val))
        else:
            cur_min = self.getMin()
            self.stack.append((val, min(cur_min, val)))


    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0] # top of the stack oth index of the tuple (num, cur_min_in_stack)
        

    def getMin(self) -> int:
        return self.stack[-1][1] # return the top of the stack (num, cur_min_in_stack)
        
