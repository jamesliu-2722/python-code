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
    def swap(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head == None or head.next == None:
            return head
        firstPair = True
        current = head
        prevSave = None
        while current != None and current.next != None:
            temp = current.next.next
            prev = current
            current = current.next
            if firstPair:
                head = current
                firstPair = False
            current.next = prev
            if prevSave:
                prevSave.next = current
            prevSave = prev
            prev.next = temp
            current = temp
        return head

head = Node(1, None, None, None)

n2 = Node(2, head, None, None)
head.next = n2

n3 = Node(3, n2, None, None)
n2.next = n3

n4 = Node(4, n3, None, None)
n3.next = n4



current = Solution().swap(head)
while current:
    print(current.val)
    current = current.next
