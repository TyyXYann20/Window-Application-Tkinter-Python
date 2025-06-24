import tkinter as tk


window = tk.Tk()
window.title("Discount Example")
window.geometry("250x150")

# Row 0
subLabel = tk.Label(window, text="Subtotal:", width=15)
subEntry = tk.Entry(window, width=20)
subLabel.grid(row=0, column=0)
subEntry.grid(row=0, column=1)
# Row 1
perLabel = tk.Label(window, text="Dicount Percent", width=15)
perEntry = tk.Entry(window, width=20)
perLabel.grid(row=1, column=0)
perEntry.grid(row=1, column=1)
# Row 2
disLabel = tk.Label(window, text="Dicount Amount", width=15)
disEntry = tk.Entry(window, width=20)
disLabel.grid(row=2, column=0)
disEntry.grid(row=2, column=1)
# Row 3
totalLabel = tk.Label(window, text="Total:", width=15)
totalEntry = tk.Entry(window, width=20)
totalLabel.grid(row=3, column=0)
totalEntry.grid(row=3, column=1)

# Event
def exit_app():
    window.quit()
    
def calculate():
    subtotal =float(subEntry.get())
    discount = perEntry.get()
    # if '%' in discount:
    #     discount = discount.replace('%', '')

    if discount.endswith('%'):
        discount = discount[:-1]
    
    discount_percent = float(discount)
    discount_amount = subtotal * (discount_percent/100)
    total = subtotal - discount_amount

    disEntry.delete(0, tk.END)
    disEntry.insert(0, f"{discount_amount:.2f}$")
    
    totalEntry.delete(0, tk.END)
    totalEntry.insert(0, f"{total:.2f}$")
    
#Row 4(Button)
exitBtn = tk.Button(window, text="Exit", width=10, 
                    background="red", fg="white",
                    cursor="hand2", command=exit_app)
calBtn = tk.Button(window, text="Calculate", width=10, 
                   background="green", fg="white",
                   cursor="hand2", command=calculate)
exitBtn.grid(row=4, column=1)
calBtn.grid(row=4, column=0)


window.mainloop()