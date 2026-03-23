from preloaded import Node


def linked_list_from_string(list_repr: str) -> Node | None:
    if list_repr == "None":
        return None

    lst = list_repr.split(" -> ")
    head = Node(int(lst[0]))
    current = head

    for val in lst[1:-1]:
        current.next = Node(int(val))
        current = current.next

    return head
