import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.geometry("300x160")
window.title("Calculate letter grade")

numLabel = tk.Label(window,text="Numeric Grade")
gradeLabel = tk.Label(window,text="Letter Grade")

entryNum = tk.Entry(window, width=15)
entryGrade = tk.Entry(window, width=15)

calBtn = tk.Button(window, text="Calculate grade", width=12, height=3)
exitBtn = tk.Button(window, text="Exit", width=12, height=3)

# row 0
numLabel.grid(row=0, column=0)
entryNum.grid(row=0, column=1)
#row 1
gradeLabel.grid(row=1, column=0)
entryGrade.grid(row=1, column=1)
# row 2

calBtn.grid(row=2, column=0, padx=10, pady=15)
exitBtn.grid(row=2, column=1,  padx=10, pady=15)

window.mainloop()