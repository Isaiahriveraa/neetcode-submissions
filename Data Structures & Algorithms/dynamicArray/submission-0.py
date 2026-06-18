class DynamicArray:
    
    def __init__(self, capacity: int):
        self.arr = [0] * capacity
        self.size = 0
        self.cap = capacity

    def get(self, i: int) -> int:
        return self.arr[i]

    def set(self, i: int, n: int) -> None:
        self.arr[i] = n

    def pushback(self, n: int) -> None:
        if self.size == self.cap:
            self.resize()

        self.arr[self.size] = n
        self.size += 1

    def popback(self) -> int:
        if self.size > 0:
            self.size -= 1
        return self.arr[self.size]
         
    def resize(self) -> None:
        self.new_arr = [0] * (self.cap * 2)
        for i, n in enumerate(self.arr):
            self.new_arr[i] = n
        
        self.arr = self.new_arr
        self.cap *= 2

    def getSize(self) -> int:
        return self.size
        
    
    def getCapacity(self) -> int:
        return self.cap

    """
    init arr = null [] len 1
    pushback 1 -> [1]

    [] len 1, 0, 1, add (1) = [1] size = 1, cap= 1, [1,2,0,0]
    ["Array", 1, "getSize", "getCapacity", "pushback", 1, "getSize", "getCapacity", "pushback", 2, "getSize", "getCapacity", "get", 1, "set", 1, 3, "get", 1, "popback", "getSize", "getCapacity"]
    [null,0,1,null,1,1,null,2,2,0,null,3,2,1,2]
    [null,0,1,null,1,1,null,2,2,2,null,3,3,1,2]

    """