import tkinter as tk


window = tk.Tk()
window.geometry("400x400")
window.title("Key")

def handle_key(event):
    key = event.char
    if key.isdigit():
        print(f"User clicked: {key}")
    

def backSpace(event=None):
    print("User Pressed Backspace")

def escape(event=None):
    print(f"User pressed Escape")
    
    
window.bind('<Key>', handle_key )
window.bind('<BackSpace>', backSpace)
window.bind('<Escape>', escape)

window.mainloop()
