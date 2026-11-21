class AVLNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 0  # a new node is a leaf


# ---------- Height helpers ----------
def get_height(node):
    return node.height if node else -1


def get_balance(node):
    if node is None:
        return 0
    return get_height(node.left) - get_height(node.right)


def update_height(node):
    node.height = 1 + max(get_height(node.left), get_height(node.right))


# ---------- Rotations ----------
def rotate_right(z):
    y = z.left
    T = y.right

    y.right = z  # z goes down
    z.left = T  # T gets a new home

    update_height(z)  # lower node first
    update_height(y)
    return y  # new top


def rotate_left(z):
    y = z.right
    T = y.left

    y.left = z
    z.right = T

    update_height(z)
    update_height(y)
    return y


# ---------- Rebalance ----------
def rebalance(node):
    update_height(node)
    bf = get_balance(node)

    if bf > 1:  # left heavy
        if get_balance(node.left) < 0:  # LR zig-zag
            node.left = rotate_left(node.left)
        return rotate_right(node)  # LL

    if bf < -1:  # right heavy
        if get_balance(node.right) > 0:  # RL zig-zag
            node.right = rotate_right(node.right)
        return rotate_left(node)  # RR

    return node  # already balanced


# ---------- Insert ----------
def insert(node, key):
    if node is None:
        return AVLNode(key)
    if key < node.key:
        node.left = insert(node.left, key)
    elif key > node.key:
        node.right = insert(node.right, key)
    else:
        return node  # duplicate ignored
    return rebalance(node)


# ---------- Delete ----------
def find_min(node):
    while node.left:
        node = node.left
    return node


def delete(node, key):
    if node is None:
        return None
    if key < node.key:
        node.left = delete(node.left, key)
    elif key > node.key:
        node.right = delete(node.right, key)
    else:
        if node.left is None:
            return node.right
        if node.right is None:
            return node.left
        succ = find_min(node.right)
        node.key = succ.key
        node.right = delete(node.right, succ.key)
    return rebalance(node)


# ---------- Search ----------
def search(node, key):
    while node and node.key != key:
        node = node.left if key < node.key else node.right
    return node


# ---------- Traversals ----------
def inorder(node):
    if node is None:
        return []
    return inorder(node.left) + [node.key] + inorder(node.right)


def preorder(node):
    if node is None:
        return []
    return [node.key] + preorder(node.left) + preorder(node.right)


# ---------- Verify the AVL property ----------
def is_avl(node):
    if node is None:
        return True
    if abs(get_balance(node)) > 1:
        return False
    return is_avl(node.left) and is_avl(node.right)


# ---------- Demo ----------
root = None
for k in [10, 20, 30, 40, 50, 25]:
    root = insert(root, k)

print("Inorder    :", inorder(root))
print("Preorder   :", preorder(root))
print("Height     :", root.height)
print("Is AVL     :", is_avl(root))
print("Search 25  :", search(root, 25) is not None)
print("Search 99  :", search(root, 99) is not None)

root = delete(root, 10)
print("After delete 10 -> Preorder:", preorder(root), "| Is AVL:", is_avl(root))

# Sorted insert test: a plain BST would become a chain of height 99
big = None
for k in range(1, 101):
    big = insert(big, k)
print("100 sorted inserts -> height:", big.height, "| Is AVL:", is_avl(big))
