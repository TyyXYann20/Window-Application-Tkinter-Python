import tkinter as tk

window = tk.Tk()
window.geometry("500x400")
window.title("Grid")

# window.columnconfigure(0, weight=1)
# window.columnconfigure(1, weight=1)

window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=2)


label1 = tk.Label(window, text="First row", bg="green", font=(20))
label2 = tk.Label(window, text="First row", bg="orange", font=(20))

label3 = tk.Label(window, text="Second row", bg="red", font=(20))
label4 = tk.Label(window, text="Second row", bg="purple", font=(20))

window.rowconfigure(0, weight=1)
window.rowconfigure(1, weight=5)
#row 1
label1.grid(row=0, column=0, sticky="news")
label2.grid(row=0, column=1, sticky="news")
#row 2
label3.grid(row=1, column=0, sticky="news")
label4.grid(row=1, column=1, sticky="news")



window.mainloop()