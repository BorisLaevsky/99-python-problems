import SingleLinkedList

def get_last(list):
    if list.next_element():
        return get_last(list.next_element())
    else:
        return list.value()

x = SingleLinkedList.Node(1, None)
print get_last(x)
