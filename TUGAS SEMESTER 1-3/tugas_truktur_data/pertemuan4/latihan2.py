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
            return None

def reverse_string(input_str):
    stack = Stack()
    # Memasukkan setiap karakter ke dalam stack
    for char in input_str:
        stack.push(char)
    # Mengambil karakter dari stack untuk membalik string
    reversed_str = ""
    while not stack.is_empty():
        reversed_str += stack.pop()
    return reversed_str

# Penggunaan
input_str = "hello"
print("String asli:", input_str)  # Output: hello
print("String setelah dibalik:", reverse_string(input_str))  # Output: olleh