
class Dequeue:
    """
    A Dequeue is a double ended queue
    Add and remove from both ends
    No direct policy

    Oldest item is in the center of the list
    Newest items are located at the ends
    """

    def __init__(self):
        """ Creates an empty deqeue """
        self.items = []

    def add_front(self, item):
        """ Adds item to the start of the dequeue """
        self.items.insert(0, item)

    def add_end(self, item):
        """ Adds item to the end of the dequeue """
        self.items.append(item)

    def remove_front(self):
        """ Removes and returns the first item """
        return self.items.pop(0)

    def remove_end(self):
        """ Removes and returns the item at the end of the dequeue """
        return self.items.pop()

    def is_empty(self):
        """ Returns whether the dequeue is empty or not """
        return self.items == []

    def size(self):
        """ Returns the size of the dequeue """
        return len(self.items)
