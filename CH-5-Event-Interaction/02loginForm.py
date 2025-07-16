import tkinter as tk

window = tk.Tk()
window.title("Simple Login Form")
window.geometry("380x240")

max_attempts = 3
attempt_count = 0

def submit_action():
    global attempt_count
    email = email_entry.get().strip()
    password = password_entry.get().strip()
    
    if not email or not password:
        message_label.config(text="Please fill in both fields", font=("Calibri", 15),
                             fg="red")
        return
    
    if ('@' not in email or
        email.startswith('@') or 
        email.endswith('@') or
        email[0].isdigit() or
        email[-1].isdigit()
        ):
        attempt_count +=1
        remaining = max_attempts - attempt_count
        if remaining > 0:
             message_label.config(text=f"Invalid email format, {remaining} attempt(s) left",
                                  fg="red",
                             font=('Calibri', 15))
             return 
        else:
            disable_form()
            message_label.config(text=f"Too many failed attempts.\n Form is locked",
                                  fg="red",
                             font=('Calibri', 20, 'bold'))
            return
            
    disable_form()
    message_label.config(text="Logged in your account", fg="green",
                             font=('Calibri', 15, 'bold'))
    

def disable_form():
    email_entry.grid_remove()
    email_label.grid_remove()
    password_entry.grid_remove()
    password_label.grid_remove()
    title_label.grid_remove()
    btnLogin.grid_remove()

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
disBtn = tk.Button(window, text="Disable Form", font=("Arial", 12), cursor="hand2",
                   bg="red", command=disable_form)

message_label = tk.Label(window, text="", fg="red", font=(12))

email_label.grid(row=1, column=0)
password_label.grid(row=2, column=0)
email_entry.grid(row=1, column=1)
password_entry.grid(row=2, column=1)
btnLogin.grid(row=3, column=1)
# disBtn.grid(row=3, column=0)

message_label.grid(row=4, column=0, columnspan=2)

window.mainloop()