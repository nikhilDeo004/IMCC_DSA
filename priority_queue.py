class node:
    def __init__(self,value,pr):
        self.next=None

class PriorityQueue:
    def __init__(Self):
        self.front=self.rear=None

    def enqueue(self,new_node):
        if self.front.priority>new_node.priority:
            new_node.next=self.front
            self.front=new_node
            return 
        else:
            temp=self.front
            while temp:
                if new_node.priority<=temp.priority:
                    break
                else:
                    prev=temp
                    temp=temp.next
            prev.next=new_node
            new_node.next=temp

    def display(self):
        temp=self.front



pq=PriorityQueue()
pq.enqueue(node(100,2))
pq.enqueue(node(100,6))
