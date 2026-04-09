class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class PriorityQueue:
    def __init__(self):
        self.front = None
        self.rear = None

    def is_empty(self):
        return self.front is None

    def enqueue(self, item, priority=False):
        new_node = Node(item)
        if priority:
            new_node.next = self.front
            self.front = new_node
            if self.rear is None:
                self.rear = new_node
        else:
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

# Contoh Penggunaan
pq = PriorityQueue()
pq.enqueue("Tugas Biasa 1", False)
pq.enqueue("Tugas Mendesak 1", True)
pq.enqueue("Tugas Biasa 2", False)
pq.enqueue("Tugas Mendesak 2", True)
print("Antrian:")
pq.display()