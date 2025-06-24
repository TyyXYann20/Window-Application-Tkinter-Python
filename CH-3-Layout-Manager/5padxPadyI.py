import tkinter as tk


window = tk.Tk()
window.title("Margin and Padding")
window.geometry("500x400")

label1 = tk.Label(window, text="Padx and Pady", font=("Arial", 20),
                  fg="red", bg="gray")

label2 = tk.Label(window, text="Ipadx and Iady", font=("Arial", 20),
                  fg="green", bg="pink")

label1.grid(row=0, column=0, padx=60,  pady=40)
label2.grid(row=1, column=0, ipadx=60, ipady=60)



window.mainloop()