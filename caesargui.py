import tkinter as tk
from tkinter import ttk

# Fungsi enkripsi menggunakan algoritma Caesar Cipher
def enkripsi(plain_text, shift):
    cipher_text = ""
    for char in plain_text:
        if char.isupper():
            cipher_text += chr((ord(char) + shift - 65) % 26 + 65)
        elif char.islower():
            cipher_text += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            cipher_text += char
    return cipher_text

# Fungsi deskripsi menggunakan algoritma Caesar Cipher
def deskripsi(cipher_text, shift):
    plain_text = ""
    for char in cipher_text:
        if char.isupper():
            plain_text += chr((ord(char) - shift - 65) % 26 + 65)
        elif char.islower():
            plain_text += chr((ord(char) - shift - 97) % 26 + 97)
        else:
            plain_text += char
    return plain_text

# Fungsi untuk memproses teks berdasarkan pilihan enkripsi atau deskripsi
def proses_teks():
    text = text_input.get("1.0", tk.END).strip()
    shift = int(entry_shift.get())
    if var.get() == 1:
        result = enkripsi(text, shift)
    else:
        result = deskripsi(text, shift)
    text_output.delete("1.0", tk.END)
    text_output.insert(tk.END, result)

# Setup GUI
root = tk.Tk()
root.title("Caesar Cipher Encryption Machine")
root.geometry("1000x1000")  # Ukuran layar disesuaikan
root.resizable(True, True)  # Membuat aplikasi bisa disesuaikan
root.configure(bg="#f7edf8")  # Warna ungu pastel yang lembut

# Mengatur gaya
style = {
    "bg": "#f7edf8",  # Background pastel ungu muda
    "font": ("Arial", 14),
    "title_font": ("Arial", 28, "bold"),
    "padx": 0,
    "pady": 0,
    "btn_bg": "#B39DDB",  # Warna ungu gelap untuk tombol
    "btn_fg": "#FFFFFF",  # Warna putih untuk teks tombol
    "entry_bg": "#ffffff",  # Background input pastel
    "input_fg": "#331637",  # Warna teks input lebih gelap
    "frame_bg": "#e6c8e9",  # Background frame input/output
    "text_height": 8,  # Menentukan tinggi untuk kotak teks
    "text_width": 40,  # Menentukan lebar untuk kotak teks
}

# Frame utama di tengah
frame_main = tk.Frame(root, bg=style["bg"], padx=40, pady=40)
frame_main.pack(fill=tk.BOTH, expand=True)

# Judul aplikasi
label_title = tk.Label(frame_main, text="Cipher Encryption Machine", bg=style["bg"], font=style["title_font"], fg="#B39DDB")
label_title.grid(row=0, column=0, columnspan=2, pady=(10, 30), sticky="nsew")

# Menambahakan pengaturan agar frame utama mengisi ruang secara fleksibel
frame_main.grid_rowconfigure(0, weight=1)  # Membuat baris pertama bisa mengembang
frame_main.grid_columnconfigure(0, weight=1)  # Membuat kolom pertama bisa mengembang
frame_main.grid_columnconfigure(1, weight=1)  # Membuat kolom kedua bisa mengembang

# Frame untuk nilai shift di atas
frame_shift = tk.Frame(frame_main, bg=style["bg"])
frame_shift.grid(row=1, column=0, columnspan=2, padx=style["padx"], pady=(10), sticky="w")

label_shift = tk.Label(frame_shift, text="Set Shift Value:", bg=style["bg"], font=style["font"], fg="#4A148C")
label_shift.pack(side=tk.LEFT)

entry_shift = tk.Entry(frame_shift, width=6, font=style["font"], bg=style["entry_bg"], justify="center", fg="#331637")
entry_shift.pack(side=tk.LEFT, padx=10)

# Frame untuk input dan output teks sejajar di bawah, memastikan berada di tengah
frame_input_output = tk.Frame(frame_main, bg=style["bg"], padx=20, pady=20)
frame_input_output.grid(row=2, column=0, columnspan=2, padx=20, pady=30, sticky="nsew")

# Menambahkan pengaturan untuk memastikan row dan column bisa mengembang dengan baik
frame_main.grid_rowconfigure(2, weight=1)  # Mengizinkan baris 2 untuk mengembang
frame_main.grid_columnconfigure(0, weight=1)  # Mengizinkan kolom 0 untuk mengembang
frame_main.grid_columnconfigure(1, weight=1)  # Mengizinkan kolom 1 untuk mengembang

# Bagian input teks
frame_input = tk.Frame(frame_input_output, bg=style["frame_bg"], bd=3, relief="solid", padx=10, pady=10)
frame_input.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")

label_input = tk.Label(frame_input, text="Input Text to Encrypt/Decrypt:", bg=style["frame_bg"], font=style["font"], fg="#4A148C")
label_input.pack(anchor="w")

# Menyesuaikan lebar dan tinggi input agar lebih kecil dan sama dengan output
text_input = tk.Text(frame_input, height=style["text_height"], width=style["text_width"], font=style["font"], bg=style["entry_bg"], fg=style["input_fg"], wrap=tk.WORD)
text_input.pack(padx=style["padx"], pady=style["pady"])

# Bagian output teks
frame_output = tk.Frame(frame_input_output, bg=style["frame_bg"], bd=3, relief="solid", padx=10, pady=10)
frame_output.grid(row=0, column=1, padx=20, pady=20, sticky="nsew")

label_output = tk.Label(frame_output, text="Output:", bg=style["frame_bg"], font=style["font"], fg="#4A148C")
label_output.pack(anchor="w")

# Menyesuaikan lebar dan tinggi output agar lebih kecil dan sama dengan input
text_output = tk.Text(frame_output, height=style["text_height"], width=style["text_width"], font=style["font"], bg=style["entry_bg"], fg=style["input_fg"], wrap=tk.WORD)
text_output.pack(padx=style["padx"], pady=style["pady"])

# Menambahkan pengaturan untuk grid dalam frame_input_output agar kolom-kolom bisa mengembang
frame_input_output.grid_rowconfigure(0, weight=1)  # Baris 0 dalam frame_input_output bisa mengembang
frame_input_output.grid_columnconfigure(0, weight=1)  # Kolom 0 dalam frame_input_output bisa mengembang
frame_input_output.grid_columnconfigure(1, weight=1)  # Kolom 1 dalam frame_input_output bisa mengembang


# Tombol dan pilihan enkripsi/deskripsi
frame_buttons = tk.Frame(frame_main, bg=style["bg"])
frame_buttons.grid(row=3, column=0, columnspan=2, padx=style["padx"], pady=style["pady"])

var = tk.IntVar()
var.set(1)

# Fungsi hover untuk pilihan enkripsi/deskripsi
def on_enter_radio(event):
    event.widget.config(bg="#9575CD", fg="white")

def on_leave_radio(event):
    event.widget.config(bg=style["bg"], fg="#4A148C")

# Menempatkan pilihan Enkripsi dan Deskripsi di tengah dengan pack() dan memberikan gaya tambahan
radio_encrypt = tk.Radiobutton(
    frame_buttons, text="Encrypt", variable=var, value=1, font=style["font"], 
    fg="#4A148C", bg=style["bg"], selectcolor="#E6C8E9", indicatoron=0, 
    width=10, height=2, bd=2, relief="solid"
)
radio_encrypt.pack(side=tk.LEFT, padx=10, pady=10)
radio_encrypt.bind("<Enter>", on_enter_radio)
radio_encrypt.bind("<Leave>", on_leave_radio)

radio_decrypt = tk.Radiobutton(
    frame_buttons, text="Decrypt", variable=var, value=2, font=style["font"], 
    fg="#4A148C", bg=style["bg"], selectcolor="#E6C8E9", indicatoron=0, 
    width=10, height=2, bd=2, relief="solid"
)
radio_decrypt.pack(side=tk.LEFT, padx=10, pady=10)
radio_decrypt.bind("<Enter>", on_enter_radio)
radio_decrypt.bind("<Leave>", on_leave_radio)


# Tombol untuk proses enkripsi/deskripsi
button_process = tk.Button(frame_buttons, text="Process Text", command=proses_teks, font=("Arial", 16), bg=style["btn_bg"], fg=style["btn_fg"], relief="raised", width=20)
button_process.pack(pady=20)

# Menambahkan animasi hover untuk tombol
def on_enter(event):
    event.widget.config(bg="#9575CD")

def on_leave(event):
    event.widget.config(bg=style["btn_bg"])

button_process.bind("<Enter>", on_enter)
button_process.bind("<Leave>", on_leave)

# Mengatur frame_buttons agar berada di tengah
frame_buttons.grid_rowconfigure(0, weight=1)  # Memastikan baris 0 memiliki bobot 1 agar komponen terpusat
frame_buttons.grid_columnconfigure(0, weight=1)  # Memastikan kolom 0 memiliki bobot 1 agar komponen terpusat
frame_buttons.grid_columnconfigure(1, weight=1)  # Memastikan kolom 1 memiliki bobot 1 agar komponen terpusat

# Menjalankan loop utama GUI
root.mainloop()
