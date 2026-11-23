from collections import deque

class TreeNode:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

class BinaryTree:
    def __init__(self):
        self.root=None

    def insert(self,val):
        new_node=TreeNode(val):
        if self.root is None:
            self.root = new_node
            return
        queue=deque([self.root])
        while queue:
            node=queue.popleft()
            