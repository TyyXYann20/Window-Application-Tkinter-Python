import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.geometry("600x400")
window.title("Frame Example-1")

window.columnconfigure((0,1), weight=1)
window.rowconfigure(0, weight=3)
window.rowconfigure(1, weight=1)

frame1 = tk.Frame(window, relief="solid", background="green",
                   borderwidth=1)
frame2 = tk.Frame(window, borderwidth=1, bg="lightblue",
                  relief="solid")
frame3 = tk.Frame(window, borderwidth=1, bg="lightyellow",
                  relief="solid")
frame4 = tk.Frame(window, borderwidth=1, bg="lightyellow",
                  relief="solid")

# widget for Frame (Label, text)
frame1.columnconfigure((0,1), weight=1)
frame1.rowconfigure(0, weight=1)
frame1.rowconfigure(1, weight=3)
label1 = tk.Label(frame1, text="Label from Frame-1",
                  font=("Arial", 20))
entry1 = tk.Entry(frame1)
label1.grid(row=0, column=0, pady=10)
entry1.grid(row=1, column=1, pady=10)


frame1.grid(row=0, column=0, sticky="news")
frame2.grid(row=0, column=1, sticky="news")
frame3.grid(row=1, column=0, sticky="news")
frame4.grid(row=1, column=1, sticky="news")

window.mainloop()