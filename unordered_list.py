
from node import ListNode

class UnorderedList:
    """
    An unordered list contains nodes that are connected to the next node
    New items are added to the front of the list (Head)
    The List tracks the head, and the head node references the next node
    """
    
    def __init__(self):
        """ Creates a new unordered list with no head """
        self.head = None
    
    def isEmpty(self):
        """ returns whether there is anything in the list """
        return self.head == None

    def add(self, item):
        """
        Creates a new node
        Adds the new node's next node as the current head node
        Sets the list's head node to the new node
        Essentiall adding an item to the front of the list, regardless of it's contents
        """
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp

    def length(self):
        """ Cycles through all nodes in the list and counting how many are there """
        current = self.head
        count = 0
        while current != Node:
            count += 1
            current = current.getNext()

        return count

    def search(self, item):
        """ Linearlly searches through the nodes from the head to the item specified """
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()

        return found

    def pop(self, item):
        """
        Tracks what node it is on and the previous node
        Searches for the node containing the item
        If the item is found it removes the node
        If the previous node is None, the next node becomes the head node of the list
        If the previous node is not None, the next node become's the previous's next node
        """
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()

        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())


