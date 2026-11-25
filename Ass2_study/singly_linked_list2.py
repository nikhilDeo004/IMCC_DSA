class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def insert_at_beginning(self, data):
        new = Node(data)
        new.next = self.head
        self.head = new

    def insert_at_end(self, data):
        new = Node(data)
        if self.head is None:
            self.head = new
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new

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
        new = Node(data)
        new.next = temp.next
        temp.next = new

    def delete_first(self):
        if self.head is None:
            print("List is empty")
            return
        self.head = self.head.next

    def delete_last(self):
        if self.head is None:
            print("List is empty")
            return
        if self.head.next is None:
            self.head = None
            return
        temp = self.head
        while temp.next.next:
            temp = temp.next
        temp.next = None

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

    def search(self, key):
        temp, idx = self.head, 0
        while temp:
            if temp.data == key:
                return idx
            temp = temp.next
            idx += 1
        return -1


# ---------- Demo ----------
ll = SinglyLinkedList()
ll.insert_at_end(20)
ll.insert_at_beginning(10)
ll.insert_at_end(30)
ll.insert_at_position(99, 2)
ll.display()                  # 10 -> 20 -> 99 -> 30 -> None
print(ll.search(99))          # 2
print(ll.search(500))         # -1
ll.delete_first()
ll.delete_last()
ll.display()                  # 20 -> 99 -> None