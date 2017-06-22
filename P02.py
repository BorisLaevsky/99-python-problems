import SingleLinkedList

def my_but_last(list):
    if list.next_element().next_element():
        return my_but_last(list.next_element())
    else:
        output = []
        output.append(list)
        output.append(list.next_element())
        return output

x = SingleLinkedList.Node(1, SingleLinkedList.Node(2, SingleLinkedList.Node(3, None)))
for element in my_but_last(x):
    print element

