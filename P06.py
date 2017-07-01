import SingleLinkedList
import P05
import copy

def is_palindrome(input_list):
    list_copy = copy.deepcopy(input_list)
    reverse_list = P05.reverse_list(list_copy)
    while input_list:
        print input_list.value(), reverse_list.value()
        if input_list.value() == reverse_list.value():
            input_list = input_list.next_element()
            reverse_list = reverse_list.next_element()
        else:
            return False
    return True

x = SingleLinkedList.Node(1, SingleLinkedList.Node(2, SingleLinkedList.Node(2, SingleLinkedList.Node(1, None))))
print is_palindrome(x)
print x.next_element()
