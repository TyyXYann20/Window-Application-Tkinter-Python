import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.geometry("500x200")
window.title("Grid Demo")

userLabel = tk.Label(window, text="Username:", font=(20))
userEntry = tk.Entry(window, width=20, font=(15))
userLabel.grid(sticky="E")
userEntry.grid(row=0, column=1)

passLabel = tk.Label(window, text="Password:", font=(20))
passEntry = tk.Entry(window, width=20, font=(15), show="*")

passLabel.grid(row=1, column=0)
passEntry.grid(row=1, column=1)

databases = ["SQL", "MySQL", "MongoDB", "Oracle", "Cassandra", "Firebase"]
comBox = ttk.Combobox(window, values=databases)
signBtn = tk.Button(window, text="Sign Up")
logBtn = tk.Button(window, text="Login")

comBox.grid(row=2, column=0)
signBtn.grid(row=2, column=1)
logBtn.grid(row=2, column=3)

window.mainloop()