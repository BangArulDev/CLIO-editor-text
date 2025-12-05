# Dokumentasi Proyek: Aplikasi Editor Teks Sederhana (CLI)

## 1. Penjelasan Desain

Aplikasi ini adalah editor teks berbasis Command Line Interface (CLI) yang dirancang untuk memenuhi tugas praktikum Struktur Data & Algoritma. Desain utama aplikasi ini memisahkan antara penyimpanan data (Model) dan logika interaksi (Controller/View).

Prinsip utama desain:

- **Penyimpanan Teks**: Menggunakan **Linked List** untuk menyimpan kata-kata.
- **Manajemen Riwayat (History)**: Menggunakan dua **Stack** (Undo Stack dan Redo Stack) untuk melacak perubahan.
- **Persistent Undo**: Jika ada aksi baru setelah Undo, riwayat Redo akan dihapus.

## 2. Struktur Data yang Digunakan

### A. Linked List (Single Linked List)

Digunakan untuk menyimpan teks utama.

- **Node**: Menyimpan satu kata dan pointer ke node berikutnya.
- **Operasi**: Insert, Delete, Display.

### B. Stack

Digunakan untuk fitur Undo dan Redo.

- **Undo Stack**: Menyimpan aksi yang dilakukan.
- **Redo Stack**: Menyimpan aksi yang dibatalkan.

### C. ActionRecord

Mencatat detail aksi (tipe aksi, indeks, data) untuk keperluan Undo/Redo.

## 3. Alur Program

1. **Inisialisasi**: Program membuat instance `TextEditor` (Linked List dan Stack kosong).
2. **Loop Utama**: Program menampilkan antarmuka TUI (Text User Interface) sederhana.
3. **Interaksi**: User menggunakan tombol keyboard untuk berinteraksi (mirip editor `vi`).
   - **Mode Normal**: Untuk navigasi dan perintah.
   - **Mode Insert**: Untuk mengetik kata.

## 4. Panduan Penggunaan (Keybindings)

### Mode Normal

- `a`: Gerakkan kursor ke **Kiri**.
- `d`: Gerakkan kursor ke **Kanan**.
- `i`: Masuk **Mode Insert** (menyisipkan setelah kursor).
- `x`: **Hapus** kata di posisi kursor.
- `u`: **Undo** (batalkan aksi).
- `r`: **Redo** (ulangi aksi).
- `:q`: **Keluar** dari program.

### Mode Insert

- Ketik kata-kata yang diinginkan.
- `Spasi` atau `Enter`: Masukkan kata ke dalam teks.
- `Backspace`: Hapus karakter yang sedang diketik.
- `ESC`: Kembali ke **Mode Normal**.

## 5. Batasan Sistem

- Data tersimpan di memori (RAM), hilang saat program ditutup.
- Operasi berbasis kata, bukan karakter individual dalam teks utama.
