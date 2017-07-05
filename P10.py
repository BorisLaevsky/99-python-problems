from SingleLinkedList import Node
from P01 import get_last
from P09 import pack

def lenght_encoding(input_list):
    output = Node(None, None)
    packed = pack(input_list)
    while packed:
        lenght = 0
        last = get_last(output)
        sublist = packed.value()
        while sublist:
            value = packed.value()
            lenght += 1
            sublist = sublist.next_element()
        last.set_next(Node(Node(lenght,Node(value, None)),None))
        packed = packed.next_element()
    return output.next_element()

x = Node(1,Node(1,Node(1,Node(1,Node(1, Node(2,Node(2,Node(2, None))))))))
print lenght_encoding(x).next_element().value().next_element()
