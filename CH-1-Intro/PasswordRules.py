import tkinter as tk

window = tk.Tk()
window.title("Entry")
window.geometry("800x600")

def is_password(password):
    if password == "":
        return True
    # 
    pass_len = len(password)
    
    if pass_len == 1:
        return password[0].isupper() 
    
    if 2 <= pass_len <= 7:
        return password[:-1].isalnum()
    
    if pass_len == 8:
        return password[-1] in "@#%"

valid_pass = (window.register(is_password), "%P")

label1 = tk.Label(window, text="Enter Password", font=(10))
label1.pack()

textBox1 = tk.Entry(window, width=50, font=(10), validate="key", validatecommand=valid_pass)
textBox1.pack()

window.mainloop()