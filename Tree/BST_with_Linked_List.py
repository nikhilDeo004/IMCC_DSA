# ---------- Part 1: Linked list (nodes use left and right) ----------
class ListNode:
    def __init__(self, val):
        self.val = val
        self.left = None                 # previous node
        self.right = None                # next node


class LinkedList:
    def __init__(self):
        self.head = None                 # first node
        self.tail = None                 # last node
        self.size = 0

    def append(self, val):               # add at the END
        new_node = ListNode(val)
        if self.head is None:            # list is empty
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.right = new_node   # old last node points right to new node
            new_node.left = self.tail    # new node points left to old last node
            self.tail = new_node
        self.size += 1

    def pop_front(self):                 # remove from the FRONT
        val = self.head.val
        self.head = self.head.right
        if self.head is None:            # list became empty
            self.tail = None
        else:
            self.head.left = None        # new first node has nothing on its left
        self.size -= 1
        return val

    def is_empty(self):
        return self.head is None

    def show(self):                      # prints like: A -> B -> C
        text = ""
        cur = self.head
        while cur:
            text += str(cur.val)
            if cur.right:
                text += " -> "
            cur = cur.right
        return text


# ---------- Part 2: Tree ----------
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def build_sample_tree():
    root = TreeNode('A')
    root.left = TreeNode('B')
    root.right = TreeNode('C')
    root.left.left = TreeNode('D')
    root.left.right = TreeNode('E')
    root.right.right = TreeNode('F')
    return root


# ---------- Part 3: DFS traversals ----------
def preorder(node, out):
    if node is None:
        return
    out.append(node.val)
    preorder(node.left, out)
    preorder(node.right, out)


def inorder(node, out):
    if node is None:
        return
    inorder(node.left, out)
    out.append(node.val)
    inorder(node.right, out)


def postorder(node, out):
    if node is None:
        return
    postorder(node.left, out)
    postorder(node.right, out)
    out.append(node.val)


# ---------- Part 4: Level order ----------
def level_order(root):
    result = LinkedList()                # a list of levels
    if root is None:
        return result

    queue = LinkedList()                 # same class works as a queue
    queue.append(root)

    while not queue.is_empty():
        level = LinkedList()
        count = queue.size               # nodes in the current level
        for _ in range(count):
            node = queue.pop_front()
            level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        result.append(level)
    return result


# ---------- Part 5: Height and counting ----------
def height(node):
    if node is None:
        return -1
    return 1 + max(height(node.left), height(node.right))


def count_nodes(node):
    if node is None:
        return 0
    return 1 + count_nodes(node.left) + count_nodes(node.right)


def count_leaves(node):
    if node is None:
        return 0
    if node.left is None and node.right is None:
        return 1
    return count_leaves(node.left) + count_leaves(node.right)


# ---------- Part 6: Report ----------
def show_levels(levels):
    text = ""
    cur = levels.head
    while cur:
        text += "[" + cur.val.show() + "]"   # cur.val is itself a LinkedList
        if cur.right:
            text += " "
        cur = cur.right
    return text


def tree_report(root):
    pre = LinkedList()
    preorder(root, pre)

    ino = LinkedList()
    inorder(root, ino)

    post = LinkedList()
    postorder(root, post)

    print("Preorder   :", pre.show())
    print("Inorder    :", ino.show())
    print("Postorder  :", post.show())
    print("Level order:", show_levels(level_order(root)))
    print("Height     :", height(root))
    print("Total nodes:", count_nodes(root))
    print("Leaf nodes :", count_leaves(root))


root = build_sample_tree()
tree_report(root)