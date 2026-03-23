class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None


class Context(object):
    def __init__(self, first, second):
        self.first = first
        self.second = second


def alternating_split(head):
    if head is None or head.next is None:
        raise ValueError("list is too short")
    first = head
    second = head.next
    curr_first = first
    curr_second = second
    current = head.next.next
    legit = True
    while current:
        if legit:
            curr_first.next = current
            curr_first = curr_first.next
        else:
            curr_second.next = current
            curr_second = curr_second.next

        current = current.next
        legit = not legit
    curr_first.next = None
    curr_second.next = None

    return Context(first, second)
