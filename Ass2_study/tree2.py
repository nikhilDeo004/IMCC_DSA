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

        if self.root is None:
            self.root=new_node
            return

        temp=self.root
        while temp:
            if data < temp.data:
                if temp.left is None:
                    temp.left = new_node
                    return
                else:
                    temp = temp.left
            if data > temp.data:
                if temp.right is None:
                    temp.right=new_node
                    return
                else:
                    temp=temp.right

    def search(self,data):
        if self.root is None:
            print("Tree is empty")
        temp=self.root
        while temp:
            if data == temp.data:
                print(data," is present")
                return
            elif data < temp.data:
                temp=temp.left
            else:
                temp=temp.right

        print(data," not found")

    def minimum(self):
        if self.root is None:
            print("No tree exists")
        temp=self.root
        while temp.left:
            temp=temp.left
        print(temp)

    def maximum(self):
        if self.root is None:
            print("No tree")
        temp=self.root
        while temp.right:
            temp=temp.right
        print(temp)

    def height(self):
        if self.root is None:
            print("No tree")
            return
        temp=self.root
        return 1+max(self.height(temp.left),self.height(temp.right))

    def count_leaves(self):
        if self.root is None:
            print("No tree")
            return
        temp=self.root
        return 1-(self.count_leaves(temp.left))+(self.count_leaves(temp.right))
            


            

    