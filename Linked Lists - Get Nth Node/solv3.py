from preloaded import Node

# class Node(object):
#     """Node class for reference"""
#     def __init__(self, data, next=None):
#         self.data = data
#         self.next = next


def get_nth(node, index):
    if not node:
        raise VallueError("Linkedlist is empty")
    i = 0
    curr = node
    while i != index:
        if not curr.next:
            raise IndexError("out of range")
        curr = curr.next
        i += 1
    return curr
