import SingleLinkedList

def find_k_element(list, k):
    if k == 0:
        return list
    else:
        return find_k_element(list.next_element(), k-1)

x = SingleLinkedList.Node(1, SingleLinkedList.Node(2, SingleLinkedList.Node(3, None)))
print find_k_element(x, 2)
