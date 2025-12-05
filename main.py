import msvcrt
import os
from editor import TextEditor

class ClioEditor:
    def __init__(self):
        self.editor = TextEditor()
        self.cursor_index = 0
        self.mode = "NORMAL"
        self.input_buffer = ""
        self.message = ""

    def clear_screen(self):
        # Bersihkan layar terminal
        os.system('cls' if os.name == 'nt' else 'clear')

    def get_text_words(self):
        # Ambil list kata dari Linked List
        words = []
        current = self.editor.text_list.head
        while current:
            words.append(current.data)
            current = current.next
        return words

    def render(self):
        # Tampilkan antarmuka editor
        self.clear_screen()
        words = self.get_text_words()
        
        if self.cursor_index < 0: self.cursor_index = 0
        if self.cursor_index > len(words): self.cursor_index = len(words)

        print("=== CLIO editor text ===")
        print(f"Mode: {self.mode} | Words: {len(words)}")
        print("-" * 40)
        
        display_str = ""
        for i, word in enumerate(words):
            if i == self.cursor_index and self.mode == "NORMAL":
                display_str += f"[{word}] "
            else:
                display_str += f"{word} "
        
        if self.cursor_index == len(words) and self.mode == "NORMAL":
            display_str += "[_]"

        print(display_str)
        
        if self.mode == "INSERT":
            print(f"\nBuffer: {self.input_buffer}_")
        
        print("-" * 40)
        if self.message:
            print(f"Msg: {self.message}")
            self.message = ""

    def handle_normal_input(self):
        # Handle input di Mode Normal
        key = msvcrt.getch()
        
        # Navigasi
        if key == b'a': # Kiri
            if self.cursor_index > 0:
                self.cursor_index -= 1
        elif key == b'd': # Kanan
            max_idx = self.editor.text_list.get_length()
            if self.cursor_index < max_idx:
                self.cursor_index += 1
        
        # Ganti Mode
        elif key == b'i': # Insert setelah kursor
            if self.cursor_index < self.editor.text_list.get_length():
                self.cursor_index += 1
            self.mode = "INSERT"
            self.message = "-- INSERT --"
            
        # Aksi
        elif key == b'x': # Hapus
            try:
                self.editor.delete(self.cursor_index)
                length = self.editor.text_list.get_length()
                if self.cursor_index >= length and length > 0:
                    self.cursor_index = length - 1
                self.message = "Menghapus kata"
            except Exception:
                self.message = "Tidak ada kata untuk dihapus"
                
        elif key == b'u': # Undo
            self.editor.undo()
            self.message = "Membatalkan aksi"
            
        elif key == b'r': # Redo
            self.editor.redo()
            self.message = "Mengulangi aksi"
            
        elif key == b':': # Command (Keluar)
            print("\n:", end='', flush=True)
            cmd = ""
            while True:
                k = msvcrt.getch()
                if k == b'\r':
                    break
                try:
                    char = k.decode('utf-8')
                    cmd += char
                    print(char, end='', flush=True)
                except: pass
            
            if cmd == 'q':
                return False
            else:
                self.message = f"Perintah tidak dikenal: {cmd}"
                
        return True

    def handle_insert_input(self):
        # Handle input di Mode Insert
        key = msvcrt.getch()
        
        if key == b'\x1b': # ESC
            self.mode = "NORMAL"
            self.input_buffer = ""
            if self.cursor_index > 0:
                self.cursor_index -= 1
            self.message = "-- NORMAL --"
            
        elif key == b' ' or key == b'\r': # Spasi/Enter untuk input kata
            if self.input_buffer:
                self.editor.insert(self.cursor_index, self.input_buffer)
                self.cursor_index += 1
                self.input_buffer = ""
                self.message = "menginput kata"
                
        elif key == b'\x08': # Backspace
            self.input_buffer = self.input_buffer[:-1]
            
        else:
            try:
                char = key.decode('utf-8')
                if char.isprintable():
                    self.input_buffer += char
            except:
                pass
        return True

    def run(self):
        while True:
            self.render()
            
            if self.mode == "NORMAL":
                if not self.handle_normal_input():
                    break
            elif self.mode == "INSERT":
                self.handle_insert_input()

if __name__ == "__main__":
    app = ClioEditor()
    app.run()
