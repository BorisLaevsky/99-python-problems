import SingleLinkedList

def reverse_list(input_list):
    if not input_list:
        return input_list
    else:
        previous = None
        current = input_list
        next_element = input_list
        while current:
            next_element = next_element.next_element()
            current.set_next(previous)
            previous = current
            current = next_element
        return previous


