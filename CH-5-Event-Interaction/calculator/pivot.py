import tkinter as tk
from tkinter import messagebox
from openpyxl import load_workbook

window = tk.Tk()
window.title("Register Page")
window.geometry("350x200")

tk.Label(window, text="Email:").grid(row=0, column=0, sticky="e", padx=10, pady=5)
email_entry = tk.Entry(window, width=25)
email_entry.grid(row=0, column=1, pady=5)

# Password
tk.Label(window, text="Password:").grid(row=1, column=0, sticky="e", padx=10, pady=5)
password_entry = tk.Entry(window, width=25, show="*")
password_entry.grid(row=1, column=1, pady=5)
# Confirm Password
tk.Label(window, text="Confirm Password:").grid(row=2, column=0, sticky="e", padx=10, pady=5)
confirm_entry = tk.Entry(window, width=25, show="*")
confirm_entry.grid(row=2, column=1, pady=5)
# Register Button
register_btn = tk.Button(window, text="Register", command=None, width=15)
register_btn.grid(row=3, columnspan=2, pady=15)

window.mainloop()