class Node:

   def __init__(self, value, next_element):
       self.__value = value
       self.__next_element = next_element

   def __str__(self):
       return str(self.__value)

   def next_element(self):
       return self.__next_element

   def value(self):
       return self.__value

   def set_next(self, next_element):
       self.__next_element = next_element

   def set_value(self, value_to_set):
       self.__value = value_to_set

