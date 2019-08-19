
from stack import Stack
from queue import Queue
from listnode import ListNode

""" STACK TESTING """
my_stack = Stack()
my_stack.push("Hello")
print(my_stack.peek())
my_stack.push("World")
print(my_stack.remove())
print(my_stack.length(), my_stack.is_empty())


""" QUEUE TESTING """
my_queue = Queue()
my_queue.enqueue(24)
my_queue.enqueue(78)
my_queue.enqueue("Bobby")
print(my_queue.peek())
my_queue.dequeue()
print(my_queue.peek())
print(my_queue.length(), my_queue.is_empty())


""" LISTNODE TESTING """
my_node = ListNode(12)
print(my_node.getData(), my_node.getNext())
other_node = ListNode("Hello World")
my_node.setNext(other_node)
my_node.setData(33)
print(my_node.getData(), my_node.getNext().getData())
