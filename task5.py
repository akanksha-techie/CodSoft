import tkinter as tk
from tkinter import messagebox, simpledialog
import json
import os
CONTACT_FILE = "contacts.json"
def load_contacts():
    if os.path.exists(CONTACT_FILE):
        with open(CONTACT_FILE, "r") as f:
            return json.load(f)
    return []
def save_contacts(contacts):
    with open(CONTACT_FILE, "w") as f:
        json.dump(contacts, f, indent=4)
def refresh_list():
    listbox.delete(0, tk.END)
    for contact in contacts:
        listbox.insert(tk.END, f"{contact['name']} - {contact['phone']}")
def add_contact():
    name = simpledialog.askstring("Add Contact", "Enter Name:")
    phone = simpledialog.askstring("Add Contact", "Enter Phone:")
    email = simpledialog.askstring("Add Contact", "Enter Email:")
    address = simpledialog.askstring("Add Contact", "Enter Address:")
    if name and phone:
        contacts.append({"name": name, "phone": phone, "email": email, "address": address})
        save_contacts(contacts)
        refresh_list()
    messagebox.showinfo("Success", "Contact added successfully")
def view_contact():
    selected = listbox.curselection()
    if selected:
        index = selected[0]
        contact = contacts[index]
        details = (f"Name: {contact['name']}\nPhone: {contact['phone']}\n"f"Email:{contact['email']}\nAddress: {contact['address']}")
        messagebox.showinfo("Contact Details", details)
    else:
        messagebox.showwarning("Warning", "Please select a contact to view.")
def search_contact():
    query = simpledialog.askstring("Search Contact", "Enter Name or Phone:")
    results = [c for c in contacts if query.lower() in c['name'].lower() or query in c['phone']]
    if results:
        listbox.delete(0, tk.END)
        for contact in results:
            listbox.insert(tk.END, f"{contact['name']} - {contact['phone']}")
    else:
        messagebox.showinfo("Not Found", "No matching contacts found.")
def update_contact():
    selected = listbox.curselected()
    if selected:
        index = selected[0]
        contact = contacts[index]
        contact['phone'] = simpledialog.askstring("Update Contact", "Enter new phone:", initialvalue=contact['phone'])
        contact['email'] = simpledialog.askstring("Update Contact", "Enter new email:", initialvalue=contact['email'])
        contact['address'] = simpledialog.askstring("Update Contact", "Enter new address:", initialvalue=contact['address'])
        save_contacts(contacts)
        refresh_list()
        messagebox.showinfo("Success", "Contact updated successfully!")
    else:
        messagebox.showwarning("Warning", "Please select a contact to delete.")
def delete_contact():
    selected = listbox.curselection()
    if selected:
        index = selected[0]
        del contacts[index]
        save_contacts(contacts)
        refresh_list()
        messagebox.showinfo("Success", "Contact deleted successfully!")
    else:
        messagebox.showwarning("Warning", "Please select a contact a delete.")
root = tk.Tk()
root.title("Contact Book")
root.geometry("400x400")
contacts = load_contacts()
listbox = tk.Listbox(root, width=50, height=15)
listbox.pack(pady=10)
refresh_list()
btn_frame = tk.Frame(root)
btn_frame.pack(pady=10)
tk.Button(btn_frame, text="Add", width=10, command=add_contact).grid(row=0, column=0, padx=5)
tk.Button(btn_frame, text="View", width=10, command=view_contact).grid(row=0, column=1, padx=5)
tk.Button(btn_frame, text="Search", width=10, command=search_contact).grid(row=0, column=2, padx=5)
tk.Button(btn_frame, text="Update", width=10, command=update_contact).grid(row=1, column=0, padx=5, pady=5)
tk.Button(btn_frame, text="Delete", width=10, command=delete_contact).grid(row=1, column=1, padx=5, pady=5)
tk.Button(btn_frame, text="Exit", width=10, command=root.destroy).grid(row=1, column=2, padx=5, pady=5) 
root.mainloop()                