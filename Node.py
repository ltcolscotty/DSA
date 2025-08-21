class SimpleNode():
    def __init__(self, data, pointer = None):
        self.data = data
        self.next: SimpleNode = pointer

    def __str__(self):
        return (f"Data:  {self.data} | Next: {self.next is not None}")

class DoubleNode():
    def __init__(self, data, next = None, previous = None):
        self.data = data
        self.next: DoubleNode = next
        self.previous: DoubleNode = previous

    def __str__(self):
        return (f"Data: {self.data} | Next: {self.next is not None} | Previous: {self.previous is not None}")

class BinaryNode():
    def __init__(self, data, left = None, right = None):
        self.data = data
        self.left: BinaryNode = left
        self.right: BinaryNode = right

    def __str__(self):
        return (f"Data: {self.data} | Left: {self.left is not None} | Right: {self.right is not None}")


    