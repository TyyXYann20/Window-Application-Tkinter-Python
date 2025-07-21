import tkinter as tk
from tkinter import messagebox

def on_enter(e):
    e.widget['background'] = '#d1e7dd'  
def on_leave(e):
    e.widget['background'] = 'SystemButtonFace' 
    
def calculate_letter_grade():
    student_score = int(entry_numeric.get())
    grade = ""
    if student_score >= 90 and student_score < 100:
        grade = "A"
        
    elif student_score >= 80 and student_score < 90:
        grade="B"
    elif student_score >= 70 and student_score < 80:
        grade="C"
    elif student_score >= 60 and student_score < 70:
        grade = "D"
    else:
        grade = "F"
    entry_letter.delete(0, tk.END)
    entry_letter.insert(0, grade)

root = tk.Tk()
root.title("Calculate Letter Grade")
root.geometry("300x160")


tk.Label(root, text="Numeric Grade").grid(row=0, column=0, padx=10, pady=10, sticky="e")
entry_numeric = tk.Entry(root, width=10)
entry_numeric.grid(row=0, column=1)

tk.Label(root, text="Letter Grade").grid(row=1, column=0, padx=10, pady=10, sticky="e")
entry_letter = tk.Entry(root, width=10)
entry_letter.grid(row=1, column=1)

# Buttons with hand cursor
btn_calculate = tk.Button(root, text="Calculate\nLetter Grade", width=12, height=3,
                          cursor="hand2",
                          command=calculate_letter_grade)
btn_calculate.grid(row=2, column=0, padx=10, pady=15)

btn_exit = tk.Button(root, text="Exit", width=12, height=3, cursor="hand2")
btn_exit.grid(row=2, column=1, padx=10, pady=15)

# Bind hover events
for btn in [btn_calculate, btn_exit]:
    btn.bind("<Enter>", on_enter)
    btn.bind("<Leave>", on_leave)

root.mainloop()
