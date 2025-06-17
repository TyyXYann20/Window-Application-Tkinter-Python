import tkinter as tk
from tkinter import PhotoImage

window = tk.Tk()
window.title("Button Demo")
window.geometry("500x500")
imgPath = PhotoImage(file="logo.png")

window.iconphoto(False, imgPath)

def add():
   num1 = entryNum1.get()
   num2 = entryNum2.get()
   result = int(num1) + int(num2)
   labelResult.config(text=f"Sum of {num1} + {num2} = {result}",
                      fg="red", font=(20)
                      )
   
def sub():
    num1 = entryNum1.get()
    num2 = entryNum2.get()
    result = int(num1) - int(num2)
    labelResult.config(text=f"Sub of {num1} - {num2} = {result}",
                      fg="green", font=(20)
                      )
   

labelNum1 = tk.Label(window, text="Number1", font=(20))
labelNum1.pack()
entryNum1 = tk.Entry(window, font=(20))
entryNum1.pack()

labelNum2 = tk.Label(window, text="Number2", font=(20))
labelNum2.pack()
entryNum2 = tk.Entry(window, font=(20))
entryNum2.pack()

btnAdd = tk.Button(window, text="Add", font=(20),
                   fg="#B72742", bg="#C1CDBF",
                   command=add
                   )

btnSub = tk.Button(window, text="Sub", font=(20),
                   fg="#30B727", bg="#D0E3CD",
                   command=sub
                   )
labelResult = tk.Label(window, text="Result will display here!", font=(20))

btnAdd.pack(side="left")
btnSub.pack(side="right")
labelResult.pack()

window.mainloop()