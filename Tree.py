from Node import BinaryNode
from Lists import Queue
from Lists import Stack

class GeneralTree():
    def __init__(self):
        self.root: BinaryNode = None
    
    def DFS(self, data) -> BinaryNode | None:
        if self.root is None:
            return None
        else:
            curNode = self.root
            s = Stack()
            s.push(curNode)

            while not s.isEmpty():
                curNode: BinaryNode = s.pop()

                if curNode.data == data:
                    return curNode
                else:
                    if curNode.left is not None:
                        s.push(curNode.left)
                    
                    if curNode.right is not None:
                        s.push(curNode.right)

    def BFS(self, data) -> BinaryNode | None:
        if self.root is None:
            return None
        else:
            curNode = self.root
            q = Queue()
            q.push(curNode)

            while not q.isEmpty():
                curNode: BinaryNode = q.pop()

                if curNode.data == data:
                    return curNode
                else:

                    if curNode.left is not None:
                        q.push(curNode.left)
                    
                    if curNode.right is not None:
                        q.push(curNode.right)
            
            return None
    
    def printOriginArray(self):
        if self.root is None:
            print("N/A")
        else:
            curNode = self.root
            q = Queue()
            q.push(curNode)

            while not q.isEmpty():
                curNode = q.pop()

                print(curNode.data)

                if curNode.left is not None:
                    q.push(curNode.left)
                
                if curNode.right is not None:
                    q.push(curNode.right)
            
            return None



class BinarySearchTree():
    """
    BST - Not guaranteed to be balanced; Duplicate keys is NOT allowed
    """
    def __init__(self):
        self.root = None

    def insert(self, data: int | float):
        newNode = BinaryNode(data)
        if self.root is None:
            self.root = newNode
        else:
            curNode = self.root
            spot = False
            while not spot:
                if data < self.root.data:
                    if curNode.left is not None:
                        curNode = curNode.left
                    else:
                        curNode.left = newNode
                        spot = True

                elif data > self.root.data:
                    if curNode.right is not None:
                        curNode = curNode.right
                    else:
                        curNode.right = newNode
                        spot = True
                else:
                    # No definitive behavior
                    spot = True
            
            return

    def search(self, data: int | float) -> bool:
        pass

    def remove(self, data: int | float):
        pass
