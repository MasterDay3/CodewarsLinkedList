from preloaded import Node


def swap_pairs(head):
    idk = Node(0)
    idk.next = head
    prev = idk
    current = head

    while current and current.next:
        nxt = current.next
        current.next = nxt.next
        nxt.next = current
        prev.next = nxt
        prev = current
        current = current.next

    return idk.next
