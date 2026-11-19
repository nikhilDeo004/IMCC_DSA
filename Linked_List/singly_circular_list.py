class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class SinglyCircularLinkedList:
    def __init__(self):
        self.head=Node

    def is_empty(self):
        if self.head is None :
            return True
        else:
            return False
        
    def insert_at_beginning(self,data):
        new_node=Node(data)
        if self.is_empty():
            self.head=new_node
            new_node.next=new_node
        else:
            last=self.head
            while last.next!=self.head:
                last=last.next
            new_node.next=self.head
            last.next=new_node
            self.head=new_node

    def insert_at_end(self, data):
    new_node = Node(data)
    if self.is_empty():
        self.head = new_node
        new_node.next = new_node
    else:
        last = self.head
        while last.next != self.head:
            last = last.next

        new_node.next = self.head
        last.next = new_node



