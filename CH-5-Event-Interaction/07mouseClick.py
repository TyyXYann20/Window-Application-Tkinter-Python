import tkinter as tk

# 3 mode:
# window.bind('<Button-1>', handle) left click
# window.bind('<Button-3>', handle) Right click
# window.bind('<Button-2>', handle) Middle click(Scroll)

window = tk.Tk()
window.geometry("400x400")
window.title("Mouse")

status_label = tk.Label(
    window,
    text="User clicked:",
    font=('Arial', 20, 'bold'),
    bg="yellow"
    
)

status_label.pack(pady=20)

def left_click(event):
    print(f"Left Click: X:{event.x} and Y:{event.y}")
def right_click(event):
    print(f"Right Click: X:{event.x} and Y:{event.y}")
    
def middle_click(event):
     print(f"Scroll: X:{event.x} and Y:{event.y}")

window.bind('<Button-1>', left_click)
window.bind('<Button-2>', middle_click)
window.bind('<Button-3>', right_click)


window.mainloop()
