import tkinter as tk

window = tk.Tk()
window.geometry("1000x500")
window.title("Text Widget")

textBox1 = tk.Text(window, width=20, height=10)
textBox1.pack()

textBox2 = tk.Text(window, width=20, height=10, font=("Arial", 10))
textBox2.pack()




window.mainloop()