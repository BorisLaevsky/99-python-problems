from SingleLinkedList import Node
from P01 import get_last

def compress(input_list):
    output = Node(None, None)
    while input_list.next_element():
        if input_list.value() != input_list.next_element().value():
            get_last(output).set_next(Node(input_list.value(), None))
        input_list = input_list.next_element()
    if input_list.value() != get_last(output).value():
        get_last(output).set_next(input_list)
    return output.next_element()

x = Node(1,Node(3,Node(3,Node(3,Node(3, None)))))
print compress(x).next_element().next_element()
