import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.geometry("400x400")
window.title("Frame Example-2")

window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=3)
window.rowconfigure(0, weight=1)

leftFrame = tk.Frame(window, relief="solid", borderwidth=1,
                     bg="lightgreen")
rightFrame = tk.Frame(window, relief="solid", borderwidth=1,
                     bg="lightblue")
leftFrame.grid(row=0, column=0, sticky="news")
rightFrame.grid(row=0, column=1, sticky="news")

# leftFrame 
leftFrame.columnconfigure(0, weight=1)
btn1Left = tk.Button(leftFrame, text="Button-1",
                     borderwidth=1, relief="groove",
                     cursor="hand2")
btn2Left = tk.Button(leftFrame, text="Button-2",
                     borderwidth=1, relief="groove",
                     cursor="hand2")
btn1Left.grid(row=0, column=0, pady=20)
btn2Left.grid(row=1, column=0, pady=20)

# rightFrame
rightFrame.columnconfigure(0, weight=1)
rightFrame.rowconfigure(0, weight=1)
rightFrame.rowconfigure(1, weight=2)

rightLabel = tk.Label(rightFrame, text="Enter message here", bg="purple",
                      fg="white", borderwidth=1)
textBox = tk.Text(rightFrame, width=30, height=20, borderwidth=1)

rightLabel.grid(row=0, column=0)
textBox.grid(row=1, column=0)
window.mainloop()