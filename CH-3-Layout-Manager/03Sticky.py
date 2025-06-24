import tkinter as tk



window = tk.Tk()
window.geometry("500x400")
window.title("Sticky")

window.columnconfigure((0,1), weight=1)
window.columnconfigure(2, weight=2)

window.rowconfigure(0, weight=1)
window.rowconfigure(1, weight=2)

emptyRow = tk.Label(window, text="Nothing", bg="pink")


col_0 = tk.Label(window, text="Column 0", bg="green", fg="white")
col_1 = tk.Label(window, text="Column 1", bg="black", fg="white")
col_2 = tk.Label(window, text="Column 2", bg="red", fg="white")

emptyRow.grid(row=0, column=0, columnspan=3, sticky="news")

col_0.grid(row=1, column=0, sticky="ns")
col_1.grid(row=1, column=1, sticky="ew")
col_2.grid(row=1, column=2, sticky="news")


window.mainloop()