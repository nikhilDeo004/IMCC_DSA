# CLASS Node:
#     METHOD initialize(data):
#         STORE data in node
#         SET next to None
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# CLASS LinkedList:
#     METHOD initialize():
#         SET head to None
class LinkedList:
    def __init__(self):
        self.head = None

#     METHOD insert_at_beginning(data):
#         CREATE new_node with data
#         SET new_node.next to head
#         SET head to new_node
    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

#     METHOD insert_at_end(data):
#         CREATE new_node with data
#         IF head is None:
#             SET head to new_node
#             RETURN
#         SET temp to head
#         WHILE temp.next is not None:
#             MOVE temp to temp.next
#         SET temp.next to new_node
    def insert_at_end(self,data):
        new_node=Node(data)



#     METHOD display():
#         SET temp to head

#         WHILE temp is not None:
#             PRINT temp.data followed by an arrow
#             MOVE temp to temp.next

#         PRINT None


#     METHOD search(key):
#         SET temp to head

#         WHILE temp is not None:
#             IF temp.data equals key:
#                 RETURN True

#             MOVE temp to temp.next

#         RETURN False


#     METHOD delete_at_beginning():
#         IF head is None:
#             PRINT "List is empty"
#             RETURN

#         MOVE head to head.next


#     METHOD delete_at_end():
#         IF head is None:
#             PRINT "List is empty"
#             RETURN

#         IF head.next is None:
#             SET head to None
#             RETURN

#         SET temp to head

#         WHILE temp.next.next is not None:
#             MOVE temp to temp.next

#         SET temp.next to None


#     METHOD insert_at_position(pos, data):
#         IF pos is less than 1:
#             PRINT "Invalid position"
#             RETURN

#         CREATE new_node with data

#         IF pos equals 1:
#             SET new_node.next to head
#             SET head to new_node
#             RETURN

#         SET temp to head
#         SET current_pos to 1

#         WHILE temp is not None AND current_pos is less than pos - 1:
#             MOVE temp to temp.next
#             INCREASE current_pos by 1

#         IF temp is None:
#             PRINT "Position out of range"
#             RETURN

#         SET new_node.next to temp.next
#         SET temp.next to new_node


# MAIN PROGRAM:
#     CREATE a LinkedList object

#     INSERT values at the beginning
#     INSERT values at the end
#     DISPLAY the list

#     SEARCH for a value
#     PRINT the search result

#     DELETE the first node
#     DELETE the last node

#     INSERT a value at a specific position
#     DISPLAY the updated list