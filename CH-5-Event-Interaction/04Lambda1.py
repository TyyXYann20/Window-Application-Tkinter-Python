import tkinter as tk
import random

window = tk.Tk()
window.geometry("1200x600")
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
def changeSize(size):
    labelNum.config(font=("Arial", size))


labelNum = tk.Label(window, text=f"Num value:", font=("Arial", 20))
plusBtn = tk.Button(window, text="Click here!", cursor="hand2",font=("Arial", 15),
                    command=increaseValue)

colorBtn = tk.Button(window, text="Change color", cursor="hand2",font=("Arial", 15),
                    command=changeColor)


size30Btn = tk.Button(window, text="fontSize: 30", cursor="hand2",font=("Arial", 15),
                    command=lambda: changeSize(30))
size50Btn = tk.Button(window, text="fontSize: 50", cursor="hand2",font=("Arial", 15),
                    command= lambda: changeSize(50))
size70Btn = tk.Button(window, text="fontSize: 70", cursor="hand2",font=("Arial", 15),
                    command=lambda:changeSize(70))
size90Btn = tk.Button(window, text="fontSize: 90", cursor="hand2",font=("Arial", 15),
                    command=lambda:changeSize(90))


labelNum.pack(pady=20)
plusBtn.pack(pady=10)
colorBtn.pack(pady=10)

# change size
size30Btn.pack(pady=10)
size50Btn.pack(pady=10)
size70Btn.pack(pady=10)
size90Btn.pack(pady=10)



window.mainloop()