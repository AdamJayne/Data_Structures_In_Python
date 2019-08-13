
class Queue:
    """
    A Queue operates with a FIFO policy
    FIRST IN FIRST OUT

    This implementation uses the front at the front of the list
    Oldest item = first in the list
    Newest item = last item in the list
    """

    def __init__(self):
        """ Creates an empty Queue """
        self.items = []

    def enqueue(self, item):
        """ Adds item to the end of the queue """
        self.items.append(item)

    def dequeue(self):
        """ Removes and returns the item at the front of the queue """
        return self.items.pop(0)

    def is_empty(self):
        """ Checks if the queue is empty """
        return self.items == []

    def peek(self):
        """ Checks the next item of the queue """
        return self.items[0]

    def length(self):
        """ Checks how long the queue is """
        return len(self.items)
