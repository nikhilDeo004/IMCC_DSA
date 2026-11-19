class Node:
    def __init__(self, value):
        self.prev = None
        self.data = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, new_node):
        temp = self.head
        if temp:
            while temp.next:
                temp = temp.next
            temp.next = new_node
            new_node.prev = temp
        else:
            self.head = new_node

    def print(self):
        temp = self.head
        print("List elements : ")
        while temp:
            print(temp.data, end=" <--> ")
            temp = temp.next
        print()

    def insert_at(self, new_node, pos):
        if pos == 1:
            new_node.next = self.head
            if self.head:
                self.head.prev = new_node
            self.head = new_node
            return

        temp = self.head
        count = 1
        while temp and count < pos - 1:
            temp = temp.next
            count += 1

        if temp is None:
            print("Position out of range")
            return

        new_node.next = temp.next
        new_node.prev = temp
        if temp.next:
            temp.next.prev = new_node
        temp.next = new_node


list1 = LinkedList()
list1.append(Node(12))
list1.append(Node(52))
list1.append(Node(102))
list1.print()

list1.insert_at(Node(5), 1)     # front
list1.insert_at(Node(77), 3)    # middle
list1.insert_at(Node(999), 6)   # end
list1.print()