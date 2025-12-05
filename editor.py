from structures import LinkedList, Stack

class ActionRecord:
    # Mencatat detail aksi untuk Undo/Redo
    def __init__(self, action_type, index, data):
        self.action_type = action_type
        self.index = index
        self.data = data

    def __repr__(self):
        return f"ActionRecord({self.action_type}, {self.index}, '{self.data}')"

class TextEditor:
    # Kelas utama editor
    def __init__(self):
        self.text_list = LinkedList()
        self.undo_stack = Stack()
        self.redo_stack = Stack()

    def insert(self, index, word):
        # Sisipkan kata dan catat di Undo Stack
        try:
            self.text_list.insert_at_index(index, word)
            action = ActionRecord("INSERT", index, word)
            self.undo_stack.push(action)
            # Hapus Redo Stack jika ada aksi baru
            self.redo_stack.clear()
            print(f"Berhasil menyisipkan '{word}' di indeks {index}.")
        except IndexError as e:
            print(f"Error: {e}")

    def delete(self, index):
        # Hapus kata dan catat di Undo Stack
        try:
            word_to_delete = self.text_list.get_at_index(index)
            self.text_list.delete_at_index(index)
            action = ActionRecord("DELETE", index, word_to_delete)
            self.undo_stack.push(action)
            # Hapus Redo Stack jika ada aksi baru
            self.redo_stack.clear()
            print(f"Berhasil menghapus '{word_to_delete}' dari indeks {index}.")
        except IndexError as e:
            print(f"Error: {e}")

    def undo(self):
        # Batalkan aksi terakhir
        if self.undo_stack.is_empty():
            print("Undo Stack kosong.")
            return

        action = self.undo_stack.pop()
        print(f"Undoing: {action}")

        if action.action_type == "INSERT":
            self.text_list.delete_at_index(action.index)
        elif action.action_type == "DELETE":
            self.text_list.insert_at_index(action.index, action.data)

        self.redo_stack.push(action)

    def redo(self):
        # Ulangi aksi yang di-undo
        if self.redo_stack.is_empty():
            print("Redo Stack kosong.")
            return

        action = self.redo_stack.pop()
        print(f"Redoing: {action}")

        if action.action_type == "INSERT":
            self.text_list.insert_at_index(action.index, action.data)
        elif action.action_type == "DELETE":
            self.text_list.delete_at_index(action.index)

        self.undo_stack.push(action)

    def display_text(self):
        # Tampilkan teks
        print("\nTeks Saat Ini:")
        print(self.text_list.display())
        print("-" * 20)
