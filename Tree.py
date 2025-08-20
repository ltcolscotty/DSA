from Node import BinaryNode
from Lists import Queue
from Lists import Stack

class GeneralTree():
    def __init__(self):
        self.root: BinaryNode = None
    
    def DFS(self, data) -> BinaryNode | None:
        pass

    def BFS(self, data) -> BinaryNode | None:
        if self.root == None:
            return None
        else:
            curNode = self.root
            q = Queue()
            q.push(curNode)

            while not q.isEmpty():
                curNode = q.pop()

                if curNode.data == data:
                    return curNode
                else:

                    if curNode.left != None:
                        q.push(curNode.left)
                    
                    if curNode.right != None:
                        q.push(curNode.right)
            
            return None



class BinarySearchTree():
    def __init__(self):
        self.root = None

    def insert(self, data: int | float):
        pass

    def search(self, data: int | float) -> bool:
        pass

    def remove(self, data: int | float):
        pass
