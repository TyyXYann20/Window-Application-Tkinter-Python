import tkinter as tk

def on_entry_click(event):
    """Function to clear placeholder when user clicks the entry."""
    if entry.get() == placeholder_text:
        entry.delete(0, "end")  
        entry.config(fg="black")

def on_focusout(event):
    """Function to add placeholder if entry is empty."""
    if entry.get() == "":
        entry.insert(0, placeholder_text)
        entry.config(fg="grey")

root = tk.Tk()
root.title("Placeholder Example")

placeholder_text = "Enter your name"

entry = tk.Entry(root, fg="grey")
entry.insert(0, placeholder_text)
entry.bind("<FocusIn>", on_entry_click)
entry.bind("<FocusOut>", on_focusout)
entry.pack(padx=20, pady=20)

root.mainloop()
