import tkinter as tk

window = tk.Tk()
window.title("Row & Col Layout")
window.geometry("900x500")

# Define 4 boxes matching the layout in your image
box1 = tk.Label(window, bg="green", bd=1, relief="solid")
box2 = tk.Label(window, bg="purple", bd=1, relief="solid")
box3 = tk.Label(window, bg="orange", bd=1, relief="solid")
box4 = tk.Label(window, bg="yellow", bd=1, relief="solid")

# Configure grid
window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=1)
window.columnconfigure(2, weight=2)

window.rowconfigure(0, weight=1)
window.rowconfigure(1, weight=1)

# Place boxes in grid
box1.grid(row=0, column=0, rowspan=2, sticky="nsew")  # Left full height
box2.grid(row=0, column=1, rowspan=2, sticky="nsew")  # Center full height
box3.grid(row=0, column=2, sticky="nsew")             # Top-right
box4.grid(row=1, column=2, sticky="nsew")             # Bottom-right

window.mainloop()
