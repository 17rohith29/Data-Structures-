"""
Author - Rohith
This program implements a stack
"""

class Node:
    """
    Basic structure to implement a 
    linked List type stack
    """
    def __init__(self, val):
        self.val = val
        self.next = next 

class Stack:
    """
    Stack
    Bottom - bottome of the stack
    top - top of the stack
    size - length of linked list
    """
    def __init__(self):
        """
        initializes the stack
        """
        self.bottom = None
        self.top = None
        self.size = 0
    
    def push(self,val):
        """
        Inserts value into top
        of a linked list 
        """
        node = Node(val)
        # Checking if stack is empty
        if self.bottom == None and self.top == None:
           self.bottom = node
           self.top = node
           self.size = 1 # updating size 
        # For non empty stack
        else:
            self.top.next = node
            self.top = self.top.next
            self.size += 1 # updating size

    def pop(self):
        """
        Removes the top most element
        """
        # for size = 1
        if self.size == 1:
            self.top = None
            self.bottom = None
            self.size = 0
        # for size > 1
        elif size > 1:
            cur = self.bottom
            while cur:
                if cur.next == self.top:
                    cur.next = None
                    self.top = cur
                cur = cur.next # allways exicutes

    def peek(self):
        """
        Returns the top of stack
        """
        return self.top.val if self.top else "Nothing in stack"

def main():
    """
    To test the stack
    """
    stack = Stack()
    stack.push(1)
    print(stack.peek())
    stack.pop()
    print(stack.peek())
    stack.push(2)
    print(stack.peek())

if __name__ == "__main__":
    main()
