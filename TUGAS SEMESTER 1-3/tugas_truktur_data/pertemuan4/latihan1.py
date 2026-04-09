class Stack:
    def __init__(self):
        self.stack = []

    def is_empty(self):
        return len(self.stack) == 0

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            return "Stack kosong!"

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            return "Stack kosong!"

# Penggunaan
stack = Stack()

# Push elemen ke stack
stack.push(5)
stack.push(10)
stack.push(15)

# Peek elemen teratas
print("Elemen teratas:", stack.peek())  # Output: 15

# Pop elemen dari stack
print("Pop elemen:", stack.pop())  # Output: 15
print("Pop elemen:", stack.pop())  # Output: 10
print("Pop elemen:", stack.pop())  # Output: 5
print("Pop elemen:", stack.pop())  # Output: Stack kosong!

# Cek apakah stack kosong
print("Apakah stack kosong?", stack.is_empty())  # Output: True