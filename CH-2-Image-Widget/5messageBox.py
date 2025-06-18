import tkinter as tk
from tkinter import messagebox

window = tk.Tk()
window.geometry("500x400")
window.title("Message Box")

def show_messagebox():
    messagebox.showinfo(title="User Information", message="You have logged in!")
    messagebox.showerror(title="Login Info", message="Your email or password is incorrect")
    messagebox.showwarning(title="User Login", message="Don't press A Button!")
    msg = messagebox.askretrycancel(title="Operation Failed", message="Do you want to retry?")
    messagebox.askquestion(title="Tkinter", message="Do you know Python?")
    print(msg)
    
# cursor property
# values (arrow, circle, xterm, watch, hand2, plus)
msgBtn = tk.Button(window, text="Press Here!", width=20, font=(20), 
                   bg="green", cursor="hand2",
                   command=show_messagebox)
msgBtn.pack()

window.mainloop()