# Definition for singly-linked list.
from inspect import stack
from typing import Optional, List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = []
        for s in tokens:
            if s == "+":
                st.append(st.pop() + st.pop())
            elif s == "-":
                op2 = st.pop()
                op1 = st.pop()
                st.append(op1 - op2)
            elif s == "*":
                st.append(st.pop() * st.pop())
            elif s == "/":
                divisor = st.pop()
                dividend = st.pop()
                st.append(int(dividend / divisor))
            else:
                st.append(int(s))
        return st.pop()


current = Solution().evalRPN(["2","1","+","3","*"])
print(current)