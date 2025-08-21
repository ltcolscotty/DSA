from Node import SimpleNode
from Node import DoubleNode

class LinkedList:
    def __init__(self):
        self.head: SimpleNode = None
        self.size = 0

    def __sizeof__(self):
        if self.head is None:
            return 0
        else:
            # O(N) implementation
            curNode: SimpleNode = self.head
            size = 1
            while curNode.next != None:
                size += 1
                curNode = curNode.next
            
            return size

class DoublyLinkedList:
    def __init__(self):
        self.head: DoubleNode = None
        self.size = 0
        
    def __sizeof__(self):
        if self.head is None:
            return 0
        else:
            # O(N) implementation
            curNode: SimpleNode = self.head
            size = 1
            while curNode.next != None:
                size += 1
                curNode = curNode.next
            
            return size

class Queue:
    """
    Head: New nodes go in here
    Tail: Pop takes nodes from here
    """
    def __init__(self):
        self.head: SimpleNode = None
        self.tail: SimpleNode = None
        self.size = 0

    def __sizeof__(self):
        return self.size
    
    def push(self, data):
        self.size += 1
        newNode = SimpleNode(data)

        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            curHead = self.head
            self.head = newNode
            curHead.next = newNode

    def pop(self):
        if self.tail is None:
            return None
        elif self.size == 1:
            self.size -= 1
            returnVal = self.tail.data
            self.head = None
            self.tail = None
            return returnVal
        else:
            self.size -= 1
            returnVal = self.tail.data
            self.tail = self.tail.next
            return returnVal

    def peek(self):
        return self.tail.data

    def isEmpty(self):
        return self.size == 0

class Deque:
    def __init__(self):
        self.head: DoubleNode = None
        self.tail: DoubleNode = None
        self.size = 0
    
    def __sizeof__(self):
        return self.size

    def push(self, data):
        newNode = DoubleNode(data)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            newNode.next = self.head
            self.head = newNode

    def push_right(self, data):
        newNode = DoubleNode(data)
        if self.tail is None:
            self.head = newNode
            self.tail = newNode
        else:
            newNode.next = self.tail
            self.tail = newNode

    def pop(self):
        ret_data = self.tail.data
        cur_tail = self.tail
        prev = self.tail.previous
        prev.next = None
        cur_tail.previous = None
        return ret_data


    def pop_left(self):
        pass

    def isEmpty(self):
        return self.size == 0

class Stack:
    def __init__(self):
        self.size = 0
        self.top = None

    def __sizeof__(self):
        return self.size

    def push(self, data):
        self.size += 1
        if self.top is None:
            self.top = SimpleNode(data)
        else:
            newNode = SimpleNode(data, self.top)
            self.top = newNode

    def pop(self):
        if self.size == 0:
            return None
        else:
            self.size -= 1
            returnVal = self.top.data
            self.top = self.top.next

    def peek(self, data):
        return self.top.data

    def isEmpty(self) -> bool:
        return self.size == 0