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

# Function Section
expression = "" # '12+15' also list
OPS_SET = {"*", "/", "+", "-"}

def handle_key(event):
    key = event.char
    if key.isdigit():
        append_value(key)
    elif key in OPS_SET:
        if key == "*":
            append_value( "x")
        elif key == "/":
            append_value("÷")
        else:
            append_value(key)
    else:
        pass
        

def append_value(val):
    
    global expression
    if val in ["0", "Error"]:
        expression = val #  0, 12+
    else:
        expression += val
    display_var.set(expression)

def percentage():
    global expression
    curr = display_var.get()
    try:
        result = float(curr) / 100
        display_var.set(str(round(result, 3)))
        expression = str(round(result, 3))
    except:
        display_var.set("Error")
 
def square_root():
    current = display_var.get()
    global expression
    try:
        result = round(math.sqrt(float(current)), 3)
        display_var.set(result)
        expression = str(result)
    except:
        display_var.set("Error")
def toggle_sign():
     curr = display_var.get()  
     if curr not in ["0", "Error"]:
        if curr.startswith("-"):
            display_var.set(curr[1:])
          
        else:
              display_var.set("-" + curr)
          
def calculate():
    global expression
    try:
        expr = expression.replace("x", "*").replace("÷", "/")
        result = eval(expr)
        result = int(result) if result == int(result) else round(result, 3)
        display_var.set(str(result))
        expression = str(result)
    except:
        display_var.set("Error")
        expression = ""
             
def on_click(button):
    if button == "AC":
        clear_result()
    elif button == "=":
        calculate()
        print("User pressed = Button")
        pass
    elif button == "%":
       percentage()
    elif button == "√":
        square_root()
    
    elif button == "+/-":
        toggle_sign()
    
    else:
        append_value(button) 
        
def clear_result(event=None):
    global expression
    expression = ""
    display_var.set("0")

def backspace(event=None):
    global expression
    expression = expression[:-1]
    display_var.set(expression if expression else "0")
  
    

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
        command= lambda v=value: on_click(v)
    )
    btn.grid(row=row+1, column=col, padx=1, pady=1, sticky="news")

window.bind("<Key>", handle_key)
window.bind("<BackSpace>", backspace)
window.bind("<Escape>",  clear_result)

window.mainloop()