import tkinter as tk
from tkinter import  ttk

window = tk.Tk()
window.title("Radio Demo")
window.geometry("500x200")
a = 10
b = 20
a = b
def chenage_state():
    if stateTk.get() == "disable":
        entryBox.config(state="disabled")
    else:
        entryBox.config(state="normal")
        
        
stateTk = tk.StringVar(value="disable")

radioBtn1 = tk.Radiobutton(window, text="Enable", value="normal", 
                           font=(20), variable=stateTk,
                           command=chenage_state
                           )
radioBtn1.pack()

radioBtn2 = tk.Radiobutton(window, text="Disable", value="disable", 
                           font=(20), variable=stateTk,
                           command=chenage_state
                           )
radioBtn2.pack()

entryBox = tk.Entry(window, width=30, state="disable", font=(20))
entryBox.pack()

window.mainloop()