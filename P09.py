from SingleLinkedList import Node
from P01 import get_last

def pack(input_list):
    output = Node(Node(input_list.value(), None), None)
    input_list = input_list.next_element()
    if input_list:
        while input_list.next_element():
            if get_last(output).value().value() == input_list.value():
                get_last(get_last(output).value()).set_next(Node(input_list.value(), None))
            else:
                get_last(output).set_next(Node(Node(input_list.value(),None), None))
            input_list = input_list.next_element()
    if get_last(output).value().value() == input_list.value():
        get_last(get_last(output).value()).set_next(Node(input_list.value(), None))
    else:
        get_last(output).set_next(Node(Node(input_list.value(),None),None))
    return output

x = Node(1,Node(1,Node(3,Node(5,Node(5, None)))))
print pack(x).next_element().next_element()
