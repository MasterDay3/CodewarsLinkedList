def stringify(node):
    """return a string using linkedlist

    ex:
    Node(1, Node(2, Node(3)))
    return "1 -> 2 -> 3 -> None"
    """
    s = ""
    t = node
    while t:
        s += str(t.data)
        t = t.next
        s += " -> "

    s += "None"
    return s
