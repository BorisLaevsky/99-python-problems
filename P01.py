import SingleLinkedList

def get_last(input_list):
    if input_list.next_element():
        return get_last(input_list.next_element())
    else:
        return input_list



