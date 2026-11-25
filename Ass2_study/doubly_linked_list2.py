class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        return self.head is None

    def insert_at_beginning(self, data):
        new = Node(data)
        if self.head is None:
            self.head = new
            self.tail = new
        else:
            new.next = self.head
            self.head.prev = new
            self.head = new

    def insert_at_end(self, data):
        new = Node(data)
        if self.head is None:
            self.head = new
            self.tail = new
        else:
            self.tail.next = new
            new.prev = self.tail
            self.tail = new

    def insert_at_position(self, data, pos):
        if pos < 0:
            print("Invalid position")
            return
        if pos == 0:
            self.insert_at_beginning(data)
            return
        temp = self.head
        for _ in range(pos - 1):
            if temp is None:
                break
            temp = temp.next
        if temp is None:
            print("Position out of range")
            return
        if temp.next is None:
            self.insert_at_end(data)
            return
        new = Node(data)
        new.prev = temp
        new.next = temp.next
        temp.next.prev = new
        temp.next = new

    def delete_first(self):
        if self.head is None:
            print("List is empty")
            return
        if self.head.next is None:
            self.head = None
            self.tail = None
            return
        self.head = self.head.next
        self.head.prev = None

    def delete_last(self):
        if self.head is None:
            print("List is empty")
            return
        if self.head.next is None:
            self.head = None
            self.tail = None
            return
        self.tail = self.tail.prev
        self.tail.next = None

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" <-> ")
            temp = temp.next
        print("None")

    def display_reverse(self):
        temp = self.tail
        while temp:
            print(temp.data, end=" <-> ")
            temp = temp.prev
        print("None")

    def search(self, key):
        temp = self.head
        idx = 0
        while temp:
            if temp.data == key:
                return idx
            temp = temp.next
            idx += 1
        return -1


# ---------- Demo ----------
dll = DoublyLinkedList()
dll.insert_at_end(20)
dll.insert_at_beginning(10)
dll.insert_at_end(30)
dll.insert_at_position(99, 2)

print("Forward :", end=" ")
dll.display()
print("Backward:", end=" ")
dll.display_reverse()

print("Search 99 :", dll.search(99))
print("Search 500:", dll.search(500))

dll.delete_first()
dll.delete_last()
print("After delete_first and delete_last:")
dll.display()
dll.display_reverse()

dll.delete_first()
dll.delete_first()
dll.delete_first()                 # empty list
print("Is empty:", dll.is_empty())