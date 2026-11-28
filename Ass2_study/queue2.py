# ---------- Part 1: Node ----------
class Node:
    def __init__(self, val):
        self.val = val
        self.right = None                # points to the node behind it


# ---------- Part 2: Queue ----------
class Queue:
    def __init__(self):
        self.front = None                # first node (leaves first)
        self.rear = None                 # last node (joined last)
        self.size = 0

    def is_empty(self):
        return self.front is None

    def enqueue(self, val):              # add at the REAR
        new_node = Node(val)
        if self.is_empty():              # first node is both front and rear
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.right = new_node   # old last node points to new node
            self.rear = new_node         # new node becomes the rear
        self.size += 1

    def dequeue(self):                   # remove from the FRONT
        if self.is_empty():
            print("Queue Underflow: nothing to dequeue")
            return None
        val = self.front.val
        self.front = self.front.right    # move front one node back
        if self.front is None:           # queue became empty
            self.rear = None
        self.size -= 1
        return val

    def peek_front(self):                # look at the front, do not remove
        if self.is_empty():
            print("Queue is empty")
            return None
        return self.front.val

    def peek_rear(self):                 # look at the rear, do not remove
        if self.is_empty():
            print("Queue is empty")
            return None
        return self.rear.val

    def get_size(self):
        return self.size

    def show(self):                      # prints from front to rear
        if self.is_empty():
            return "(empty)"
        text = ""
        cur = self.front
        while cur:
            text += str(cur.val)
            if cur.right:
                text += " -> "
            cur = cur.right
        return text


# ---------- Part 3: Demo ----------
q = Queue()
print("Is empty   :", q.is_empty())

q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
print("Queue (front first):", q.show())

print("Front      :", q.peek_front())
print("Rear       :", q.peek_rear())
print("Size       :", q.get_size())

print("Dequeue    :", q.dequeue())
print("Dequeue    :", q.dequeue())
print("Queue now  :", q.show())

print("Dequeue    :", q.dequeue())
print("Is empty   :", q.is_empty())
q.dequeue()                              # dequeue from an empty queue