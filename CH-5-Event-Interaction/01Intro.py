import tkinter as tk
import random

window = tk.Tk()
window.geometry("900x400")
window.title("Demo 1")
num=0
def increaseValue():
    global num
    labelNum.config(text=f"Num value: {num}")
    num +=1
    
def changeColor():
    colors = ['red', 'green', 'lightblue', 'blue', 'yellow', 'black',
              'purple', 'orange', 'pink', 'gold']
    
    labelNum.config(bg=random.choice(colors))
def changeSize50(size):
    labelNum.config(font=("Arial", size))
def changeSize30():
    labelNum.config(font=("Arial", 30))

labelNum = tk.Label(window, text=f"Num value:", font=("Arial", 20))
plusBtn = tk.Button(window, text="Click here!", cursor="hand2",font=("Arial", 15),
                    command=increaseValue)

colorBtn = tk.Button(window, text="Change color", cursor="hand2",font=("Arial", 15),
                    command=changeColor)

sizeBtn = tk.Button(window, text="fontSize: 50", cursor="hand2",font=("Arial", 15),
                    command=changeSize50(10))

size30Btn = tk.Button(window, text="fontSize: 30", cursor="hand2",font=("Arial", 15),
                    command=changeSize30)


labelNum.pack(pady=20)
plusBtn.pack(pady=10)
colorBtn.pack(pady=10)
size30Btn.pack(pady=10)
sizeBtn.pack(pady=10)


window.mainloop()