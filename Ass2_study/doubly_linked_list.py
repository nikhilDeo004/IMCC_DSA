class Node:
    def __init__(self,data):
        self.data=data
        self.prev=None
        self.next=None

class DoublyLinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
        self.size=0

    def is_empty(self):
        return self.head in None

    def insert_at_beginning(self, data):
            new = Node(data)
            if self.head is None:         # empty: new node is head AND tail
                self.head = self.tail = new
            else:
                new.next = self.head      # 1) new -> old head
                self.head.prev = new      # 2) old head -> new  (back link)
                self.head = new           # 3) move head
            self.size += 1

    def insert_at_end(self, data):
        new = Node(data)
        if self.head is None:
            self.head = self.tail = new
        else:
            new.prev = self.tail      # 1) new <- old tail
            self.tail.next = new      # 2) old tail -> new
            self.tail = new           # 3) move tail
        self.size += 1

    def insert_before_node(self, node, data):     # node reference is given
            if node is self.head:
                self.insert_at_beginning(data)
                return
            new = Node(data)
            new.next = node               # 1) new -> node
            new.prev = node.prev          # 2) new <- node's old prev
            node.prev.next = new          # 3) old prev -> new
            node.prev = new               # 4) node <- new
            self.size += 1
 
    def insert_at_position(self, pos, data):      # 0-indexed
        if pos < 0 or pos > self.size:
            print("Position out of range")
            return
        if pos == 0:
            self.insert_at_beginning(data)
        elif pos == self.size:
            self.insert_at_end(data)
        else:
            self.insert_before_node(self._node_at(pos), data)

    def delete_first(self):
        if self.head is None:
            print("List is empty")
            return
        if self.head is self.tail:    # only one node
            self.head = self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None     # cut the back link of the new head
        self.size -= 1

    def delete_last(self):
        if self.head is None:
            print("List is empty")
            return
        if self.head is self.tail:
            self.head = self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        self.size -= 1

    def delete_by_value(self,key):
        node=self._find(key)
        if node is None:
            print("Value not found")
            return
        self.delete_node(self._node_at(pos))