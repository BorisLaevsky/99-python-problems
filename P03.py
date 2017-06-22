import SingleLinkedList

def find_k_element(input_list, k):
    if k == 1:
        return input_list
    elif not input_list.next_element():
        return None
    else:
        return find_k_element(input_list.next_element(), k-1)

x = SingleLinkedList.Node(1, SingleLinkedList.Node(2, SingleLinkedList.Node(3, None)))
print find_k_element(x, 5)
