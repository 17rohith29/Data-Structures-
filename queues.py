"""
Author - Rohith
This program implements a queue
"""

class Node:
    """
    Basic structure to implement a 
    linked List type queue
    """
    def __init__(self, val):
        self.val = val
        self.next = next 

class Queue:
    """
    Queue
    back - back of the Queue, where
    addition takes place
    front - front of the Queue
    size - length of linked list
    """
    def __init__(self):
        """
        initializes the Queue
        """
        self.back = None
        self.front = None
        self.size = 0

    def enqueue(self, val):
    	"""
    	adds element to back of queue
    	"""
    	temp = Node(val) # creating the node 
    	if front == None and back == None:
    		self.front = temp
    		self.back = temp
    	else:
    		self.back.next = temp
    		self.back = temp

    def isEmpty(self):
    	"""
    	Returns true if queue is empty
    	"""
    	return self.front == None

    def dequeue(self):
    	"""
    	Removes element from
		front of list
		"""
		if not isEmpty():
			if self.front == self.back:
				self.front = None
				self.back = None
			else:
				self.front = self.font.next