import SingleLinkedList

def number_of_elements(input_list, index = 0):
    if not input_list:
        return index
    elif input_list.next_element():
        index += 1
        return number_of_elements(input_list.next_element(), index)
    else:
        return index + 1

x = SingleLinkedList.Node(1, SingleLinkedList.Node(2, SingleLinkedList.Node(3, None)))
y = None
print number_of_elements(y)
