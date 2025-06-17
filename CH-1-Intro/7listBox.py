import tkinter as tk
from tkinter import  ttk

window = tk.Tk()
window.title("ComboBox Demp")
window.geometry("500x400")

labelBox = tk.Label(window, text="List database:", font=(20))
labelBox.pack()

databases = ["SQL", "MySQL", "MongoDB", "Oracle", "Cassandra", "Firebase"]

# listBox = tk.Listbox(window, font=("Arial", 15),
#                      listvariable=tk.StringVar(value=databases)
#                      )
listBox = tk.Listbox(window, font=("Arial", 15), selectmode="multiple")
listBox.pack()

for data in databases:
    listBox.insert(tk.END, data)

window.mainloop()