class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

class BST:
    def __init__(self):
        self.root=None

    def insert(self,data):
        new_node=Node(data)
        if self.root==None:
            self.root=new_node
        else:
            temp=self.root

            while True:
                if new_node.data<temp.data:
                    if temp.left==None:
                        temp.left==new_node
                        return
                    else:
                        temp=temp.left
                else:
                    if temp.right==None:
                        temp.right==new_node
                        return
                    else:
                        temp=temp.right

    def preorder(self,root):
        if root == None:
            return
        else:
            print(root.data,end=" ")
            self.preorder(root.left)
            self.preorder(root.right)

    def postorder(self,root):
        if root == None:
            return
        else:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.data,end=" ")

    def inorder(self,root):
        if root == None:
            return
        else:
            self.inorder(root.left)
            print(root.data,end=" ")
            self.inorder(root.right)
            
                        



    