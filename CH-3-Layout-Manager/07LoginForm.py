import tkinter as tk


window = tk.Tk()
window.title("Login Form")
window.geometry("300x150")


window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=3)

window.rowconfigure((0, 1, 2), weight=1)
username = "Admin"
password = "123"
# col-1 Label
userLabel = tk.Label(window, text="Username:")
passLabel = tk.Label(window, text="Password:")
# col-2 EntryBOx
userEntry = tk.Entry(window)
passEntry = tk.Entry(window)
#col2 & row3
loginBtn = tk.Button(window, text="Login", relief="groove")

#place widget
userLabel.grid(row=0, column=0, sticky="w", padx=5, pady=5)
passLabel.grid(row=1, column=0, sticky="w", padx=5, pady=5)
userEntry.grid(row=0, column=1, sticky="ew" , padx=5, pady=5)
passEntry.grid(row=1, column=1, sticky="ew", padx=5, pady=5)
loginBtn.grid(row=2, column=1, sticky="e", padx=5, pady=5)



window.mainloop()