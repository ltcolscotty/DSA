class SimpleNode():
    def __init__(self, data, pointer = None):
        self.data = data
        self.next = pointer

class DoubleNode():
    def __init__(self, data, next = None, previous = None):
        self.data = data
        self.next = next
        self.previous = previous

class BinaryNode():
    def __init__(self, data, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right


    