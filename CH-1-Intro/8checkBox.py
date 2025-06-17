import tkinter as tk

window = tk.Tk()
window.title("CheckBox Demo")
window.geometry("500x500")

def check_state():
    labelBox.config(text=state.get(), fg="green", font=(20))

state = tk.StringVar()
checkBtn = tk.Checkbutton(window, text="Click Me",
                          onvalue="Tick!", offvalue="Not tick",
                          font=(15), variable=state,
                          command=check_state
                          )
checkBtn.pack()

labelBox = tk.Label(window, text="Text here:", font=(20))
labelBox.pack()

window.mainloop()