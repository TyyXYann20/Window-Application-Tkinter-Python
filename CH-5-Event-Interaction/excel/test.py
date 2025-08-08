import tkinter as tk
from tkinter import messagebox

def add_task():
    task = entry.get()
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

def delete_task():
    try:
        selected = listbox.curselection()
        listbox.delete(selected)
    except:
        messagebox.showwarning("Warning", "Please select a task to delete.")

# Main window
root = tk.Tk()
root.title("To-Do List")
root.geometry("300x400")

# Input field
entry = tk.Entry(root, width=25)
entry.pack(pady=10)

# Buttons
tk.Button(root, text="Add Task", command=add_task).pack(pady=5)
tk.Button(root, text="Delete Task", command=delete_task).pack(pady=5)

# Task list
listbox = tk.Listbox(root, width=30, height=15)
listbox.pack(pady=10)

root.mainloop()