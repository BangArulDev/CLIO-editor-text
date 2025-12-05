class Node:
    # Node untuk Linked List
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    # Implementasi Linked List untuk menyimpan teks
    def __init__(self):
        self.head = None

    def insert_at_index(self, index, data):
        # Sisipkan data pada indeks tertentu
        new_node = Node(data)
        
        if index == 0:
            new_node.next = self.head
            self.head = new_node
            return

        current = self.head
        count = 0
        
        while current is not None and count < index - 1:
            current = current.next
            count += 1
        
        if current is None:
            raise IndexError("Index out of bounds")
            
        new_node.next = current.next
        current.next = new_node

    def delete_at_index(self, index):
        # Hapus data pada indeks tertentu
        if self.head is None:
            raise IndexError("List is empty")

        if index == 0:
            self.head = self.head.next
            return

        current = self.head
        count = 0
        
        while current is not None and count < index - 1:
            current = current.next
            count += 1
            
        if current is None or current.next is None:
            raise IndexError("Index out of bounds")
            
        current.next = current.next.next

    def get_at_index(self, index):
        # Ambil data pada indeks tertentu
        current = self.head
        count = 0
        while current is not None:
            if count == index:
                return current.data
            current = current.next
            count += 1
        raise IndexError("Index out of bounds")

    def get_length(self):
        # Hitung panjang list
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

    def display(self):
        # Tampilkan seluruh isi list sebagai string
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        return " ".join(elements)

class Stack:
    # Implementasi Stack untuk Undo/Redo
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return None

    def is_empty(self):
        return len(self.items) == 0

    def clear(self):
        self.items = []
