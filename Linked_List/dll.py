class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        temp = self.head

        while temp.next is not None:
            temp = temp.next

        temp.next = new_node
        new_node.prev = temp

    def display_forward(self):
        temp = self.head

        while temp is not None:
            print(temp.data, end=" <-> ")
            temp = temp.next

        print("None")

    def display_backward(self):
        if self.head is None:
            print("List is empty")
            return

        temp = self.head

        while temp.next is not None:
            temp = temp.next

        while temp is not None:
            print(temp.data, end=" <-> ")
            temp = temp.prev

        print("None")

    def search(self, key):
        temp = self.head

        while temp is not None:
            if temp.data == key:
                return True
            temp = temp.next

        return False

    def delete_at_beginning(self):
        if self.head is None:
            print("List is empty")
            return

        self.head = self.head.next

        if self.head is not None:
            self.head.prev = None

    def delete_at_end(self):
        if self.head is None:
            print("List is empty")
            return

        if self.head.next is None:
            self.head = None
            return

        temp = self.head

        while temp.next is not None:
            temp = temp.next

        temp.prev.next = None

    def insert_at_position(self, pos, data):
        if pos < 1:
            print("Invalid Pos")
            return

        if pos == 1:
            self.insert_at_beginning(data)
            return

        if self.head is None:
            print("Position out of range")
            return

        temp = self.head
        current_pos = 1

        while temp.next is not None and current_pos < pos - 1:
            temp = temp.next
            current_pos += 1

        if current_pos != pos - 1:
            print("Position out of range")
            return

        new_node = Node(data)
        new_node.next = temp.next
        new_node.prev = temp

        if temp.next is not None:
            temp.next.prev = new_node

        temp.next = new_node

    def count_occ(self,num):
        temp=self.head
        cnt=0
        while temp:
            if temp.data==num:
                cnt+=1
            temp=temp.next

        print("The occurance : ",cnt)

    

# Main program
dll = DoublyLinkedList()

dll.insert_at_beginning(10)
dll.insert_at_beginning(20)
dll.insert_at_end(30)

print("Forward:")
dll.display_forward()

print("Backward:")
dll.display_backward()

print("Search 10:", dll.search(10))
print("Search 99:", dll.search(99))

dll.insert_at_position(3, 15)
print("After inserting 15 at position 3:")
dll.display_forward()

dll.delete_at_beginning()
print("After deleting at beginning:")
dll.display_forward()

dll.delete_at_end()
print("After deleting at end:")
dll.display_forward()

dll.count_occ(10)