class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def is_empty(self):
        return self.front is None

    def enqueue(self, item):
        new_node = Node(item)
        if self.is_empty():
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def display(self):
        temp = self.front
        while temp:
            print(temp.data, end=" -> " if temp.next else "")
            temp = temp.next
        print()

def reverse_queue(queue_obj):
    stack = []
    temp_queue = Queue()
    temp = queue_obj.front
    while temp:
        stack.append(temp.data)
        temp = temp.next
    while stack:
        temp_queue.enqueue(stack.pop())
    return temp_queue

# Contoh Penggunaan
my_queue = Queue()
my_queue.enqueue(1)
my_queue.enqueue(2)
my_queue.enqueue(3)
print("Antrian Asli:")
my_queue.display()
reversed_q = reverse_queue(my_queue)
print("Antrian Terbalik:")
reversed_q.display()
print("Antrian Asli (tidak berubah):")
my_queue.display()