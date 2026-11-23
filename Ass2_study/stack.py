# ---------- Part 1: Node ----------
class Node:
    def __init__(self, val):
        self.val = val
        self.right = None                # points to the node below it


# ---------- Part 2: Stack ----------
class Stack:
    def __init__(self):
        self.top = None                  # the top node
        self.size = 0

    def is_empty(self):
        return self.top is None

    def push(self, val):                 # add on TOP
        new_node = Node(val)
        new_node.right = self.top        # new node points to the old top
        self.top = new_node              # new node becomes the top
        self.size += 1

    def pop(self):                       # remove from TOP
        if self.is_empty():
            print("Stack Underflow: nothing to pop")
            return None
        val = self.top.val
        self.top = self.top.right        # move top down one node
        self.size -= 1
        return val

    def peek(self):                      # look at the top, do not remove
        if self.is_empty():
            print("Stack is empty")
            return None
        return self.top.val

    def get_size(self):
        return self.size

    def show(self):                      # prints from top to bottom
        if self.is_empty():
            return "(empty)"
        text = ""
        cur = self.top
        while cur:
            text += str(cur.val)
            if cur.right:
                text += " -> "
            cur = cur.right
        return text


# ---------- Part 3: Demo ----------
s = Stack()
print("Is empty :", s.is_empty())

s.push(10)
s.push(20)
s.push(30)
print("After pushing 10, 20, 30 (top first):", s.show())

print("Peek     :", s.peek())
print("Size     :", s.get_size())

print("Pop      :", s.pop())
print("Pop      :", s.pop())
print("Stack now:", s.show())

print("Pop      :", s.pop())
print("Is empty :", s.is_empty())
s.pop()                                  # pop from an empty stack