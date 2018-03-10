"""
Author - Rohith Prabakar 
This program creates an implementation of linked List
"""
class Node:
    """
    Basic Node which is used to 
    link up to form a linked list
    """
    def __init__(self, val):
        self.val = val   # initializes value
        self.next = None # the next points to
                         # another node

class LinkedList:
    """
    The Linked List implementation
    head - the begining pointer 
    size - size of linked list
    """
    def __init__(self):
        self.head = None # Creates a head Node
        self.size = 0    # Creates a size variable

    def addVal(self, nodeVal):
        '''
        adds a node to the linked list 
        nodeVal is the variable required to 
        construct a node 
        '''
        if nodeVal is None:
            print("Oops no input")
        if self.head is None:
            self.head = Node(nodeVal)
            self.size += 1 # updates size
        else:
            cur = self.head
            while cur:
                if cur.next == None:
                    cur.next = Node(nodeVal)
                    self.size += 1
                    break
                else:
                    cur = cur.next
    def __str__(self):
        """ 
        This represents the linked list as 
        a string 
        """
        cur = self.head # initializes the traverser
        result = ""     # Empty string to store  
                        # output
        while cur:
            result += str(cur.val)
            if cur.next:
                result += " " #adds space if there
                              #is element after
            cur = cur.next
        return result

    def removeFirst(self, val):
        """
        This function removes the first
        occurence of a node with a variable
        """
        # Creates a dummy head node for simplicity
        cur = Node(0)    
        cur.next = self.head
        if self.head and self.head.val == val:
            self.head = self.head.next
            return
        while cur:
            if cur.next and cur.next.val == val:
                cur.next = cur.next.next
                self.size -= 1 #update size 
                break
            else:
                cur = cur.next
#####################################################
# CODE TO TEST
def main():
    # Creates a linked list 
    lst = LinkedList()
    # adding 2 elements 
    lst.addVal(1)
    lst.addVal(2)
    # prints out list and its size 
    print(lst)
    print('The size of list is {}'.format(lst.size))
    # Removes the element 1 
    lst.removeFirst(1)
    # prints out list and its size 
    print(lst)
    print('The size of list is {}'.format(lst.size))

if __name__ == "__main__":
    main()
