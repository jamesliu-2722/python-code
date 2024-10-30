import re

class MinStack:
    bo = True
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.st = []
        self.min_st = []

    def push(self, x: int) -> None:
        self.st.append(x)
        if not self.min_st:
            self.min_st.append(x)
            return
        if self.min_st[-1] >= x:
            self.min_st.append(x)

    def pop(self) -> None:
        if self.st[-1] == self.min_st[-1]:
            self.min_st.pop()
        self.st.pop()

    def top(self) -> int:
        return self.st[-1]

    def getMin(self) -> int:
        if not self.min_st:
            return []
        return self.min_st[-1]

    def test(self, x) -> int:
        global bo
        bo = False
        y = 6
        x = 3
        return x

obj = MinStack()
bo = True
x = 2
obj.test(4)
print(bo)
obj.push(2)
obj.push(1)
obj.push(0)
print(obj.getMin())
obj.pop()
print(obj.getMin())
#
















