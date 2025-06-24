import tkinter as tk


window = tk.Tk()
window.title("Exercise II")
window.geometry("900x500")

#Define n column
window.columnconfigure((0,1), weight=1)
window.columnconfigure(2, weight=2)

window.rowconfigure((0,1), weight=1)

box1 = tk.Label(window,text="Box1", bg="green",
                bd=1, relief="solid")
box2 = tk.Label(window, text="Box2", bg="purple",
                bd=1,  relief="solid")
box3 = tk.Label(window, text="Box3", bg="orange",
                bd=1, relief="solid")
box4 = tk.Label(window, text="Box4", bg="yellow",
                bd=1, relief="solid")

box1.grid(row=0, column=0, rowspan=2, sticky="news")
box2.grid(row=0, column=1, rowspan=2, sticky="news")
box3.grid(row=0, column=2, sticky="news")
box4.grid(row=1, column=2, sticky="news")


window.mainloop()