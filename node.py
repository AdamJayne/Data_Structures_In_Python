
class ListNode:
    """
    A ListNode structure is essential for collection types

    Holds data and references other nodes
    """

    def __init__(self, data):
        """ Creates a new node with data passed in """
        self.data = data
        self.next = None
    
    def getData(self):
        """ Returns the data contained in the node """
        return self.data

    def getNext(self):
        """ Returns the next referenced node """
        return self.next

    def setData(self, data):
        """ Changes the internal data to new data """
        self.data = data

    def setNext(self, newnext):
        """ Changes the node that is referenced """
        self.next = newnext


