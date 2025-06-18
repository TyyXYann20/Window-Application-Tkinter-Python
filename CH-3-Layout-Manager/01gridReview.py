import tkinter as tk
from tkinter import messagebox

window = tk.Tk()
window.geometry("500x400")
window.title("Grid")

window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=1)
window.columnconfigure(2, weight=1)
window.columnconfigure(3, weight=3)


label1 = tk.Label(window, text="Col-0-Row-0", bg="green", font=(20))
label2 = tk.Label(window, text="Col-1-Row-0", bg="orange", font=(20))
label3 = tk.Label(window, text="Col-2-Row-0", bg="blue", font=(20))
label4 = tk.Label(window, text="Col-4-Row-0", bg="pink", font=(20))

label1.grid(row=0, column=0, sticky="ew")
label2.grid(row=0, column=1, sticky="ew")
label3.grid(row=0, column=2, sticky="ew")
label4.grid(row=0, column=3, sticky="ew")


window.mainloop()