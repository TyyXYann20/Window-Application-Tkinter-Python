import tkinter as tk

window = tk.Tk()
window.title("Entry")
window.geometry("800x600")


label1 = tk.Label(window, text="Enter Password", font=(10))
label1.pack()

textBox1 = tk.Entry(window, width=50, font=(10))
textBox1.pack()


window.mainloop()