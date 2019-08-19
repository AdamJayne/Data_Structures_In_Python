
from node import ListNode

class OrderedList:
    """
    An ordered list contains nodes that are connected in sequence
    New items are added to the list in a sorted pattern
    The item is placed between the nodes that are greater and less than the items value
    """
    
    def __init__(self):
        """ Creates a new Ordered list with no node as the head """
        self.head = None

    def isEmpty(self):
        """ Returns if there is anything in the Ordered list """
        return self.head == None

    def length(self):
        """ Cycles through all nodes in the list and returns the node count """
        current = self.head
        count = 0
        while current != None:
            count += 1
            current = current.getNext()

        return count
    
    def search(self, item):
        """ Linearlly searches through the nodes from the head for the item specified """
        current = self.head
        found = False
        stop = False
        while current != None and not found and not stop:
            if current.getData() == item:
                found = True
            else:
                if current.getDat() > item:
                    stop = True

                else:
                    current = current.getNext()

        return found

    def add(self, item):
        """
        Adds a node to the list by searching for the ordered place for the new node
        """
        current = self.head
        previous = None
        stop = False
        while current != None and not stop:
            if current.getData() > item:
                stop = True
            else:
                previous = current
                current = current.getNext()

        temp = Node(item)
        if previous == None:
            temp.setNext(self.head)
            self.head = temp
        else:
            temp.setNext(current)
            previous.setNext(temp)

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



