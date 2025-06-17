import tkinter as tk
from tkinter import  ttk

window = tk.Tk()
window.title("ComboBox Demp")
window.geometry("500x200")

labelBox = tk.Label(window, text="Select one database:", font=(20))
labelBox.pack()

databases = ["SQL", "MySQL", "MongoDB", "Oracle", "Cassandra", "Firebase"]
comboBox = ttk.Combobox(window, values=databases, width=50)
comboBox.pack()

window.mainloop()