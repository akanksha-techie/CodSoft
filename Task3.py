import tkinter as tk
from tkinter import messagebox
import random
import string
def generate_password():
    try:
        length = int(length_entry.get())
        if length < 4:
            messagebox.showwarning("Warning", "Password length should be at least 4")
            return
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(length))
        result_entry.delete(0, tk.END)
        result_entry.insert(0, password)
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number")
def copy_to_clipboard():
    password = result_entry.get()
    if password:
        window.clipboard_clear()
        window.clipboard_append(password)
        messagebox.showinfo("Copied", "Password copied to clipboard!")
    else:
        messagebox.showwarning("Warning", "No password to copy!")
window = tk.Tk()
window.title("Password Generator")
window.geometry("400x200")
window.config(bg="#e6f2ff")
tk.Label(window, text="Enter Password Length:", bg="#e6f2ff").pack(pady=10)
length_entry = tk.Entry(window)
length_entry.pack()
tk.Button(window, text="Generated Password", command=generate_password, bg="#007acc", fg="white").pack(pady=10)
tk.Label(window, text="Generated Password:", bg="#e6f2ff").pack()
result_entry = tk.Entry(window, width=30)
result_entry.pack()
tk.Button(window, text="Copy to Clipborad", command=copy_to_clipboard, bg="#28a745", fg="white").pack(pady=10)
window.mainloop()
