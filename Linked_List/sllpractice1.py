class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    # 1. Insert at the beginning
    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # 2. Insert at the end
    def insert_at_end(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        temp = self.head

        while temp.next is not None:
            temp = temp.next

        temp.next = new_node

    # 3. Display the linked list
    def display(self):
        temp = self.head

        while temp is not None:
            print(temp.data, end=" -> ")
            temp = temp.next

        print("None")

    # 4. Search for a value
    def search(self, key):
        temp = self.head

        while temp is not None:
            if temp.data == key:
                return True
            temp = temp.next

        return False

    # 5. Delete from the beginning
    def delete_at_beginning(self):
        if self.head is None:
            print("List is empty")
            return

        self.head = self.head.next

    # 6. Delete from the end
    def delete_at_end(self):
        if self.head is None:
            print("List is empty")
            return

        if self.head.next is None:
            self.head = None
            return

        temp = self.head

        while temp.next.next is not None:
            temp = temp.next

        temp.next = None

    # 7. Insert at a specific position (1-based)
    def insert_at_position(self, pos, data):
        if pos < 1:
            print("Invalid position")
            return

        new_node = Node(data)

        if pos == 1:
            new_node.next = self.head
            self.head = new_node
            return

        temp = self.head
        current_pos = 1

        while temp is not None and current_pos < pos - 1:
            temp = temp.next
            current_pos += 1

        if temp is None:
            print("Position out of range")
            return

        new_node.next = temp.next
        temp.next = new_node


# ---------- Main Program ----------

# Create a linked list
ll = LinkedList()

# Insert at the beginning
ll.insert_at_beginning(10)
ll.insert_at_beginning(20)

# Insert at the end
ll.insert_at_end(30)

print("Original list:")
ll.display()

# Search
print("Search 10:", ll.search(10))
print("Search 99:", ll.search(99))

# Insert at position 3
ll.insert_at_position(3, 15)
print("After inserting 15 at position 3:")
ll.display()

# Delete at the beginning
ll.delete_at_beginning()
print("After deleting at beginning:")
ll.display()

# Delete at the end
ll.delete_at_end()
print("After deleting at end:")
ll.display()