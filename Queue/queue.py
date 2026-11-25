class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, x):
        self.items.append(x)

    def pop(self):
        return self.items.pop()


class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    # 1. Enqueue
    def enqueue(self, x):
        self.items.append(x)

    # 2. Dequeue
    def dequeue(self):
        if self.is_empty():
            return None
        return self.items.pop(0)

    # 3. Display
    def display(self):
        if self.is_empty():
            print("Queue is empty")
        else:
            print("Queue (front to rear):", *self.items)

    # 4. Reverse the queue using stack
    def reverse(self):
        st = Stack()
        while not self.is_empty():
            st.push(self.dequeue())
        while not st.is_empty():
            self.enqueue(st.pop())


# 5. Merge two queues into one
def merge(q1, q2):
    result = Queue()
    for x in q1.items:
        result.enqueue(x)
    for x in q2.items:
        result.enqueue(x)
    return result


# 6. Check if two queues are identical
def is_identical(q1, q2):
    return q1.items == q2.items


# Predefined queues
q1 = Queue()
for x in [10, 20, 30, 40, 50]:
    q1.enqueue(x)

q2 = Queue()
for x in [60, 70, 80]:
    q2.enqueue(x)

print("1. Enqueue (10, 20, 30, 40, 50 enqueued)")
q1.display()

print("\n2. Dequeue")
print("Dequeued element:", q1.dequeue())

print("\n3. Display")
q1.display()

print("\n4. Reverse the queue using stack")
print("Before reverse:")
q1.display()
q1.reverse()
print("After reverse:")
q1.display()

print("\n5. Merge two queues into one")
print("Queue 1:", *q1.items)
print("Queue 2:", *q2.items)
merged = merge(q1, q2)
print("Merged queue:", *merged.items)

print("\n6. Check if two queues are identical")
q3 = Queue()
for x in [60, 70, 80]:
    q3.enqueue(x)
print("Queue 2:", *q2.items)
print("Queue 3:", *q3.items)
print("Queue 2 and Queue 3 identical?", is_identical(q2, q3))
print("Queue 1 and Queue 2 identical?", is_identical(q1, q2))