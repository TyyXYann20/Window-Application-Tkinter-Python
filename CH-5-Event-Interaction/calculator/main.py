import tkinter as tk
import math


window = tk.Tk()
window.title("Calculator")
window.geometry("360x540")
window.iconbitmap("D:\PyGUI\CH-5-Event-Interaction\calculator\icon.ico")
window.resizable(False, False)
window.rowconfigure(0, weight=1)
window.columnconfigure(0, weight=1)

main_frme = tk.Frame(window, bg="#1c1c1c")
main_frme.grid(sticky="news")
main_frme.rowconfigure((0,1,2,3,4), weight=1)
main_frme.columnconfigure((0,1,2,3), weight=1)

display_var = tk.StringVar(value="0")
display_res = tk.Label(
    main_frme, 
    textvariable=display_var,
    font=("Arial", 40), 
    bg="#1c1c1c",
    fg="#ffffff",
    padx=10,
    anchor="e"
    )

display_res.grid(row=0, column=0, columnspan=4, sticky="news", pady=20)

BUTTONS_VALUE = [
    "AC", "+/-", "%", "÷",
    "7", "8", "9", "x",
    "4", "5", "6", "-",
    "1", "2", "3", "+",
    "0", ".", "√", "="
]

COLS = 4
for index, value in enumerate(BUTTONS_VALUE):
    row = index // COLS
    col = index % COLS
    if value in { "AC", "+/-", "%"}:
        background, font = "#d4d4d2",  "#1c1c1c"
    elif value in {"+", "-",  "÷", "x", "="}:
        background, font = "#ff9500",  "#ffffff"
    else:
         background, font = "#505050",  "#ffffff"
        
    btn = tk.Button(
        main_frme,
        text=value,
        bg= background,
        fg= font,
        borderwidth=0,
        font=("Arial", 30),
        cursor="hand2",
        command=None
    )
    btn.grid(row=row+1, column=col, padx=1, pady=1, sticky="news")


window.mainloop()