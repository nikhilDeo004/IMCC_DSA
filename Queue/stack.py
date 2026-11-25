class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    # 1. Push
    def push(self, x):
        self.items.append(x)

    # 2. Pop
    def pop(self):
        if self.is_empty():
            return None
        return self.items.pop()

    # 3. Display
    def display(self):
        if self.is_empty():
            print("Stack is empty")
        else:
            print("Stack (top to bottom):", *reversed(self.items))

    # 5. Reverse Stack using another Stack
    def reverse_stack(self):
        temp1, temp2 = Stack(), Stack()
        while not self.is_empty():
            temp1.push(self.pop())
        while not temp1.is_empty():
            temp2.push(temp1.pop())
        while not temp2.is_empty():
            self.push(temp2.pop())


# 4. Reverse String using Stack
def reverse_string(s):
    st = Stack()
    for ch in s:
        st.push(ch)
    result = ""
    while not st.is_empty():
        result += st.pop()
    return result


# Predefined stack
s = Stack()
for x in [10, 20, 30, 40, 50]:
    s.push(x)

print("1. Push (10, 20, 30, 40, 50 pushed)")
s.display()

print("\n2. Pop")
print("Popped element:", s.pop())

print("\n3. Display")
s.display()

print("\n4. Reverse String using Stack")
text = "Hello"
print("Original string:", text)
print("Reversed string:", reverse_string(text))

print("\n5. Reverse Stack using another Stack")
print("Before reverse:")
s.display()
s.reverse_stack()
print("After reverse:")
s.display()