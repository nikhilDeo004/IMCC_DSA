class BSTNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


# ---------- Search ----------
def search(node, key):
    if node is None or node.key == key:
        return node
    if key < node.key:
        return search(node.left, key)
    return search(node.right, key)


def search_iter(node, key):
    while node and node.key != key:
        node = node.left if key < node.key else node.right
    return node


# ---------- Insert ----------
def insert(node, key):
    if node is None:
        return BSTNode(key)
    if key < node.key:
        node.left = insert(node.left, key)
    elif key > node.key:
        node.right = insert(node.right, key)
    return node          # duplicates are ignored


# ---------- Min / Max ----------
def find_min(node):
    while node.left:
        node = node.left
    return node


def find_max(node):
    while node.right:
        node = node.right
    return node


# ---------- Delete ----------
def delete(node, key):
    if node is None:
        return None
    if key < node.key:
        node.left = delete(node.left, key)
    elif key > node.key:
        node.right = delete(node.right, key)
    else:
        # Case 1 and 2: zero or one child
        if node.left is None:
            return node.right
        if node.right is None:
            return node.left
        # Case 3: two children
        succ = find_min(node.right)
        node.key = succ.key
        node.right = delete(node.right, succ.key)
    return node


# ---------- Traversal ----------
def inorder(node):
    if node is None:
        return []
    return inorder(node.left) + [node.key] + inorder(node.right)


# ---------- Validate ----------
def is_valid_bst(node, low=float('-inf'), high=float('inf')):
    if node is None:
        return True
    if not (low < node.key < high):
        return False
    return (is_valid_bst(node.left, low, node.key) and
            is_valid_bst(node.right, node.key, high))


# ---------- Demo ----------
root = None
for k in [8, 3, 10, 1, 6, 14, 4, 7, 13]:
    root = insert(root, k)

print("Inorder         :", inorder(root))
print("Search 6        :", search(root, 6) is not None)
print("Search 99       :", search(root, 99) is not None)
print("Min / Max       :", find_min(root).key, "/", find_max(root).key)
print("Valid BST       :", is_valid_bst(root))

root = delete(root, 4)      # Case 1: leaf
print("Delete 4 (leaf) :", inorder(root))

root = delete(root, 14)     # Case 2: one child
print("Delete 14 (one) :", inorder(root))

root = delete(root, 3)      # Case 3: two children
print("Delete 3 (two)  :", inorder(root))

print("Valid BST       :", is_valid_bst(root))