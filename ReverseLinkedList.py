from typing import Optional


class Node:
    def __init__(self, data, next):
        self.data = data
        self.next = next


    # def reverse(self, head):
    #     current = head
    #     prev = None
    #     while current:
    #         next_node = current.next
    #         current.next = prev
    #         prev = current
    #         current = next_node
    #     self.head = prev
def reverse_list(head):
    prev = None
    current = head
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev

# if __name__ == "__main__":

n4 = Node(4, None)
n3 = Node(3, n4)
n2 = Node(2, n3)
n1 = Node(1, n2)
head = Node(0, n1)

current = head
while current is not None:
    print(current.data)
    current = current.next

head = reverse_list(head)
current = head
while current is not None:
    print(current.data)
    current = current.next