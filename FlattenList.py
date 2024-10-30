# Definition for singly-linked list.
from inspect import stack
from typing import Optional
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        st = []
        current = head
        last = None
        while current:
            if current.child:
                st.append(current.next)
                prev = current
                current = current.child
                current.prev = prev
                prev.next = current
            else:
                last = current
                current = current.next

        current = last
        while True:
            if len(st) > 0:
                item = st.pop()
                if item:
                    current.next = item
                    current = item
                    if len(st) == 0:
                        break
                    while current.next:
                        current = current.next
                else:
                    break
        return head


head = Node(1, None, None, None)

n2 = Node(2, head, None, None)
head.next = n2

n3 = Node(3, n2, None, None)
n2.next = n3

n4 = Node(4, n3, None, None)
n3.next = n4

n5 = Node(5, n4, None, None)
n4.next = n5

n6 = Node(6, n5, None, None)
n5.next = n6

n7 = Node(7, None, None, None)
n3.child = n7

n8 = Node(8, n7, None, None)
n7.next = n8

n9 = Node(9, n8, None, None)
n8.next = n9

n10 = Node(10, n9, None, None)
n9.next = n10

n11 = Node(11, n8, None, None)
n8.child = n11

n12 = Node(12, n11, None, None)
n11.next = n12



current = Solution().flatten(head)
while current:
    print(current.val)
    current = current.next
