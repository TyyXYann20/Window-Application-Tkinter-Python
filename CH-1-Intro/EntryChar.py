import tkinter as tk

window = tk.Tk()
window.title("Entry")
window.geometry("800x600")

def only_chars(input_text):
    return input_text.isalpha() or input_text == ""

valid_func = (window.register(only_chars), '%S')
label1 = tk.Label(window, text="Enter Password", font=(10))
label1.pack()

textBox1 = tk.Entry(window, width=50, font=(10), validate="key", validatecommand=valid_func)
textBox1.pack()

window.mainloop()