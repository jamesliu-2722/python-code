# Python program to reverse a linked list
# in groups of given size

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Function to reverse K groups
def reverse_k_group(head, k):
    if head is None:
        return head

    curr = head
    new_head = None
    tail = None

    while curr is not None:
        group_head = curr
        prev = None
        next_node = None
        count = 0

        # Reverse the nodes in the current group
        while curr is not None and count < k:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
            count += 1

        # If new_head is null, set it to the
        # last node of the first group
        if new_head is None:
            new_head = prev

        # Connect the previous group to the
        # current reversed group
        if tail is not None:
            tail.next = prev

        # Move tail to the end of
        # the reversed group
        tail = group_head

    return new_head


def print_list(head):
    curr = head
    while curr is not None:
        print(curr.data, end=" ")
        curr = curr.next
    print()


if __name__ == "__main__":
    # Creating a sample singly linked list:
    # 1 -> 2 -> 3 -> 4 -> 5 -> 6
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)

    head = reverse_k_group(head, 3)
    print_list(head)