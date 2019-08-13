
class Stack:
    """
    A Stack operates with a LIFO policy
    LAST IN FIRST OUT
    
    This implementation uses the top at the end of list
    Oldest item = first in the list
    Newest item = last item in the list
    (More performant than shifting each time we remove an item)
    """

    def __init__(self):
        """ Creates an empty stack """
        self.items = []

    def push(self, item):
        """ Adds item to the top of the stack """
        self.items.append(item)

    def remove(self):
        """ Returns the last item """
        return self.items.pop()

    def is_empty(self):
        """ Checks if the stack is empty """
        return self.items == []

    def peek(self):
        """ Checks the item at the top of the stack """
        return self.items[len(self.items) - 1]

    def length(self):
        """ Checks how tall the stack is """
        return len(self.items)



