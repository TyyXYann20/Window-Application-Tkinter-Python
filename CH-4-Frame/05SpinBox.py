import tkinter as tk
from tkinter import ttk, font


window = tk.Tk()
window.geometry("600x600")
window.title("SpinBox Demo")
#print(font.families())
label = ttk.Label(window, text="Price:", font=(20))
price = ttk.Spinbox(window, width=25, from_=10, to=100, increment=5)


label.grid(row=0, column=0)
price.grid(row=0, column=1)

window.mainloop()