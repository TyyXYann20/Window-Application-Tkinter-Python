import tkinter as tk

window = tk.Tk()
window.geometry("500x300")
window.title("Grid Layout: Color Picker")
# window.config(bg="white")

COLOR_OPTIONS = [
    "red", "green", "blue", "yellow",
    "purple", "orange", "cyan", "magenta",
    "lightgray", "pink", "gold", "black"
]
# Frame for Buttons
button_frame = tk.Frame(window, bg="white", pady=10)
labelBg = tk.Label(
    window,
    text="Select Background Color:",
    font=('Helvetica', 12),
    bg="White"
)

def change_background_color(color):
    window.config(bg=color)
    button_frame.config(bg=color)
    

print(1%4)
# add widget to layout
labelBg.grid(row=0, column=0, pady=(20, 10))
button_frame.grid(row=1, column=0)

for index, color in enumerate(COLOR_OPTIONS):
    row = index // 4
    col = index % 4
    
    color_button = tk.Button(
        button_frame,
        text=color.capitalize(),
        bg=color,
        width=10,
        fg= "white" if color in ["red", "black", "blue", "purple"] else "black",
        cursor="hand2",
        command= lambda c=color: change_background_color(c)
    )
    color_button.grid(row=row, column=col, padx=5, pady=5)



window.mainloop()