class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self, values=None):
        self.head = None
        if values:
            self.create(values)

    # 1. Create linked list from an iterable
    def create(self, values):
        self.head = None
        tail = None
        for v in values:
            node = Node(v)
            if self.head is None:
                self.head = tail = node
            else:
                tail.next = node
                tail = node

    def duplicate(self):
        values = []
        cur = self.head
        while cur:
            values.append(cur.data)
            cur = cur.next
        return SinglyLinkedList(values)

    # 2. Traverse and print node values
    def traverse(self):
        values = []
        cur = self.head
        while cur:
            values.append(cur.data)
            cur = cur.next
        print(" -> ".join(map(str, values)) + " -> None" if values else "List is empty")
        return values

    # 3. Insert node at a specific position (0-based index)
    def insert_at(self, pos, value):
        if pos < 0:
            raise IndexError("Position cannot be negative")
        node = Node(value)
        if pos == 0:
            node.next = self.head
            self.head = node
            return
        cur = self.head
        for _ in range(pos - 1):
            if cur is None:
                break
            cur = cur.next
        if cur is None:
            raise IndexError("Position out of range")
        node.next = cur.next
        cur.next = node

    # 4. Find middle node (second middle if even length) and print its value
    def find_middle(self):
        """
        Return the value of the middle node.
        If the list length is even, returns the second middle node.
        Returns None if the list is empty.
        """
        # Count how many nodes the list has
        length = 0
        cur = self.head
        while cur:
            length += 1
            cur = cur.next

        if length == 0:
            print("List is empty")
            return None

        # Index of the (second) middle element (0‑based)
        middle_index = length // 2

        # Walk again to that index
        cur = self.head
        for _ in range(middle_index):
            cur = cur.next

        print("Middle node value:", cur.data)
        return cur.data
    


    # 5. Delete node by position (0-based index)
    def delete_at(self, pos):
        if self.head is None or pos < 0:
            raise IndexError("Invalid position")
        if pos == 0:
            self.head = self.head.next
            return
        cur = self.head
        for _ in range(pos - 1):
            if cur is None:
                break
            cur = cur.next
        if cur is None or cur.next is None:
            raise IndexError("Position out of range")
        cur.next = cur.next.next

    # Delete node by value (first occurrence)
    def delete_value(self, value):
        if self.head is None:
            return False
        if self.head.data == value:
            self.head = self.head.next
            return True
        cur = self.head
        while cur.next:
            if cur.next.data == value:
                cur.next = cur.next.next
                return True
            cur = cur.next
        return False

    # 6. Reverse list (iterative, O(n) time, O(1) space)
    def reverse(self):
        prev, cur = None, self.head
        while cur:
            cur.next, prev, cur = prev, cur, cur.next
        self.head = prev

    # 7. Sum of every two consecutive node values: (a1+a2), (a2+a3), ...
    def consecutive_sums(self):
        sums = []
        cur = self.head
        while cur and cur.next:
            sums.append(cur.data + cur.next.data)
            cur = cur.next
        print("Sum of consecutive pairs:", sums)
        return sums

    # 8. Delete the middle node (second middle if even length)
    def delete_middle(self):
        if self.head is None:
            print("List is empty")
            return
        prev, slow, fast = None, self.head, self.head
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        if prev is None:          # only one node
            self.head = None
        else:
            prev.next = slow.next

    # 9. Delete the first node
    def delete_first(self):
        if self.head is None:
            print("List is empty")
            return
        self.head = self.head.next

    # 10. Delete the last node
    def delete_last(self):
        if self.head is None:
            print("List is empty")
            return
        if self.head.next is None:    # only one node
            self.head = None
            return
        cur = self.head
        while cur.next.next:          # stop at the second-last node
            cur = cur.next
        cur.next = None

    # 11. Delete alternate nodes (removes 2nd, 4th, 6th ... nodes)
    def delete_alternate(self):
        cur = self.head
        while cur and cur.next:
            cur.next = cur.next.next  # skip the alternate node
            cur = cur.next


def show(original, current):
    """Print the untouched original list and the current list."""
    print("Original :", end=" ")
    original.traverse()
    print("Current  :", end=" ")
    current.traverse()


if __name__ == "__main__":
    ll = SinglyLinkedList([10, 20, 30, 40, 50])
    original = ll.duplicate()      # saved copy, never modified

    print("Start:")
    show(original, ll)

    print("\nInsert 25 at position 2:")
    ll.insert_at(2, 25)
    show(original, ll)

    print("\nMiddle node:")
    ll.find_middle()
    show(original, ll)

    print("\nDelete node at position 1:")
    ll.delete_at(1)
    show(original, ll)

    print("\nReverse:")
    ll.reverse()
    show(original, ll)

    print("\nConsecutive sums:")
    ll.consecutive_sums()
    show(original, ll)

    print("\nDelete middle:")
    ll.delete_middle()
    show(original, ll)

    print("\nDelete first node:")
    ll.delete_first()
    show(original, ll)

    print("\nDelete last node:")
    ll.delete_last()
    show(original, ll)

    # Fresh copy of the original so the alternate deletion is easy to see
    print("\nDelete alternate nodes (on a fresh copy of the original):")
    ll = original.duplicate()
    ll.delete_alternate()
    show(original, ll)