
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        new_node = Node(data)

        if self.root is None:
            self.root = new_node
            return

        temp = self.root

        while temp:
            if data < temp.data:
                if temp.left is None:
                    temp.left = new_node
                    return
                else:
                    temp = temp.left
            else:
                if temp.right is None:
                    temp.right = new_node
                    return
                else:
                    temp = temp.right

    def search(self, data):
        temp = self.root

        while temp:
            if data == temp.data:
                print(data, "is present in tree")
                return
            elif data < temp.data:
                temp = temp.left
            else:
                temp = temp.right

        print(data, "is not present in tree")

    def minimum(self):
        temp = self.root
        if temp is None:
            return

        while temp.left:
            temp = temp.left
        print(temp.data)

    def maximum(self):
        temp = self.root
        if temp is None:
            return

        while temp.right:
            temp = temp.right
        print(temp.data)

    def height(self, current):
        if current is None:
            return 0
        return 1 + max(self.height(current.left), self.height(current.right))

    def count(self, current):
        if current is None:
            return 0
        return 1 + self.count(current.left) + self.count(current.right)

    def inorder(self, current):
        if current:
            self.inorder(current.left)
            print(current.data, end=" ")
            self.inorder(current.right)

    def preorder(self, current):
        if current:
            print(current.data, end=" ")
            self.preorder(current.left)
            self.preorder(current.right)

    def postorder(self, current):
        if current:
            self.postorder(current.left)
            self.postorder(current.right)
            print(current.data, end=" ")


# Creating BST
tree = BST()

# Inserting values
values = [50, 30, 70, 20, 40]

for value in values:
    tree.insert(value)


# Searching
print("Search:")
tree.search(30)

# Minimum
print("Minimum:")
tree.minimum()

# Maximum
print("Maximum:")
tree.maximum()

# Height
print("Height:")
print(tree.height(tree.root))

# Total nodes
print("Total Nodes:")
print(tree.count(tree.root))

# Inorder
print("Inorder:")
tree.inorder(tree.root)
print()

# Preorder
print("Preorder:")
tree.preorder(tree.root)
print()

# Postorder
print("Postorder:")
tree.postorder(tree.root)
print()
