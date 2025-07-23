import tkinter as tk
from tkinter import messagebox
tasks = []
def add_task():
    task = entry.get()
    if task:
        tasks.append(task)
        update_list()
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task!")
def delete_task():
    try:
        selected = listbox.curselection()
        if not selected:
            raise IndexError
        task_index = selected[0]
        tasks.pop(task_index)
        update_list()
    except IndexError:
        messagebox.showerror("Error", "No task selected!")
def update_list():
    listbox.delete(0, tk.END)
    for i, task in enumerate(tasks,start=1):
        listbox.insert(tk.END, f"{i}.{task}")
root = tk.Tk()
root.title("To-Do List")
root.geometry("350x400")
root.configure(bg="#f0f8ff")
tk.Label(root, text="My To-Do List", font=("Arial", 16, "bold"),bg="#f0f8ff").pack(pady=10)
entry = tk.Entry(root, font=("Arial",14), width=25)
entry.pack(pady=10)
btn_frame = tk.Frame(root, bg="#f0f8ff")
btn_frame.pack()
add_btn = tk.Button(btn_frame, text="Add Task", font=("Arial", 12), width=12, command=add_task)
add_btn.grid(row=0, column=1, padx=5)
del_btn = tk.Button(btn_frame, text="Delete Task", font=("Arial",12), width=12, command=delete_task)
del_btn.grid(row=0, column=1, padx=5)
listbox = tk.Listbox(root, font=("Arial", 13),width=40, height=10, bd=4, relief="ridge")
listbox.pack(pady=15)
exit_btn = tk.Button(root, text="Exit", font=("Arial", 12),bg="#ffcccc", command=root.destroy)
exit_btn.pack(pady=5)
root.mainloop()