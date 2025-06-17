import tkinter as tk 

window = tk.Tk()
window.title("Label")
window.geometry("400x200")

label1 = tk.Label(window, text="FirstName:", font=("Arial", 20), fg="#b3b354")
label1.pack()

label2 = tk.Label(window, text="LastName:", font=("Times New Roman", 20), fg="#2a96fb")
label2.pack()

# font("font style", fontSize)
#font(size)
# bg = Background color
#fg = Font color

window.mainloop()