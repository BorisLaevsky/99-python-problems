from SingleLinkedList import Node
from P01 import get_last

def flat(input_list):
    output = Node(None, None)
    while input_list:
        if isinstance(input_list.value(), Node):
            get_last(output).set_next(flat(input_list.value()))
        else:
            get_last(output).set_next(Node(input_list.value(), None))
        input_list = input_list.next_element()
    return output.next_element()

x = Node(1, Node(Node(Node(2, None), Node(Node(3, Node(4, None)), None)), Node(5, Node(6, None))))
s = flat(x)
print s.next_element().next_element().value()
