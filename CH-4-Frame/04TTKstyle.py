import tkinter as tk
from tkinter import ttk, font

#  Label => TLabel , bg => background, fg => foreground, font
# TButton
# target
# style.config('label1.TLabel', ...)
# style.config('label2.TLabel', ...)

# label1 pink font:Jokerman
# label2 lightblue
# label3 lightyellow
window = tk.Tk()
window.geometry("600x600")
window.title("TTK Style")
#print(font.families())
style = ttk.Style()

style.configure('label1.TLabel', background="pink", foreground="black",
                font=('Jokerman', 20))
style.configure('label2.TLabel', background="lightblue", foreground="black",
                font=('Khmer OS Moul', 20))
style.configure('label3.TLabel', background="lightyellow", foreground="black",
                font=('Khmer OS Moul', 20))
style.configure('TButton', font=('Jokerman', 20))
style.map('TButton', foreground=[('pressed', 'red'), ('disabled', 'green')],
          background=[('pressed', 'green'), ('active', 'blue')]
          )

label1 = ttk.Label(window, text="This is Label 1",
                   style="label1.TLabel")
label2 = ttk.Label(window, text="កម្ពុជា ឆ្ពោះទៅកាន់អធិរាជស្វាយចន្ទី",
                   style="label2.TLabel")
label3 = ttk.Label(window, text="តោះទៅ",
                   style="label3.TLabel")

btnSub = ttk.Button(window, text="Update", cursor="hand2")
btnDel = ttk.Button(window, text="Delete", cursor="hand2")


label1.pack(pady=20)
label2.pack(pady=20)
label3.pack(pady=20)
btnDel.pack(pady=10)
btnSub.pack(pady=10)




window.mainloop()