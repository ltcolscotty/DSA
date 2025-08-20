class SimpleNode():
    def __init__(self, data, pointer = None):
        self.data = data
        self.next = pointer

    def __str__(self):
        return (f"Data:  {self.data} | Next: {self.next is not None}")

class DoubleNode():
    def __init__(self, data, next = None, previous = None):
        self.data = data
        self.next = next
        self.previous = previous

    def __str__(self):
        return (f"Data: {self.data} | Next: {self.next is not None} | Previous: {self.previous is not None}")

class BinaryNode():
    def __init__(self, data, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        return (f"Data: {self.data} | Left: {self.left is not None} | Right: {self.right is not None}")


    