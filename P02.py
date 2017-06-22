import SingleLinkedList

def my_but_last(input_list):
    if input_list.next_element().next_element():
        return my_but_last(input_list.next_element())
    else:
        return input_list


x = SingleLinkedList.Node(1, SingleLinkedList.Node(2, SingleLinkedList.Node(3, None)))
print my_but_last(x)
