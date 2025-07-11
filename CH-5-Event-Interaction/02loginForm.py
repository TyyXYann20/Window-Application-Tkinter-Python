import tkinter as tk

window = tk.Tk()
window.title("Simple Login Form")
window.geometry("380x240")

def submit_action():
    email = email_entry.get().strip()
    password = password_entry.get().strip()
    
    if not email or not password:
        message_label.config(text="Please fill in both fields", font=("Calibri", 15),
                             fg="red")
        return
    
    if '@' not in email or email.startswith('@') or email.endswith('@'):
        message_label.config(text="Invalid email format", fg="red",
                             font=('Calibri', 15))
        return 
    message_label.config(text="Logged in your account", fg="green",
                             font=('Calibri', 15))
    



fontLabel = ("Segeo UI", 12, "bold")
title_label = tk.Label(window, text="Login Form", font=("Arial", 20, "bold"))
title_label.grid(row=0, column=0, columnspan=2)

# Input Field
email_label = tk.Label(window, text="Email:", font=fontLabel )
password_label = tk.Label(window, text="Password:", font=fontLabel )

email_entry = tk.Entry(window, font=(14), width=25)
password_entry = tk.Entry(window, font=(14), width=25, show="*")

btnLogin = tk.Button(window, text="Login", font=("Arial", 12),
                     command=submit_action)
message_label = tk.Label(window, text="", fg="red", font=(12))

email_label.grid(row=1, column=0)
password_label.grid(row=2, column=0)
email_entry.grid(row=1, column=1)
password_entry.grid(row=2, column=1)
btnLogin.grid(row=3, column=1)
message_label.grid(row=4, column=0, columnspan=2)

window.mainloop()