import tkinter as tk
from tkinter import ttk


window = tk.Tk()
window.geometry("500x400")
window.title("Frame Layout")

window.columnconfigure(1, weight=1)
window.rowconfigure(1, weight=1)

header_frame = tk.Frame(window, relief="solid", borderwidth=1)
navbar_frame = tk.Frame(window, relief="solid", borderwidth=1)
main_content_frame = tk.Frame(window, relief="solid", borderwidth=1)
#add Frame to the root app

#Header Frame
header_frame.grid(row=0, column=0, columnspan=2, sticky="ew", padx=5, pady=5)
header_frame.columnconfigure(0, weight=1)
header_label = tk.Label(header_frame, text="Application Header",
                        font=("Helvetiica", 14))
header_label.grid(row=0, column=0)

# Nav and Main content
navbar_frame.grid(row=1, column=0, padx=5, pady=5, sticky="ns")
main_content_frame.grid(row=1, column=1,  padx=5, pady=5, sticky="news")



# define row and column
header_frame.columnconfigure(0, weight=1)
navbar_frame.columnconfigure(0, weight=1)
main_content_frame.columnconfigure(0, weight=1)
main_content_frame.rowconfigure(1, weight=1)

# add button to navbar
nav_btn1 = tk.Button(navbar_frame, text="Navigation 1")
nav_btn2 = tk.Button(navbar_frame, text="Navigation 2")
nav_btn1.grid(row=0, column=0, sticky="ew", padx=10, pady=10)
nav_btn2.grid(row=1, column=0, sticky="ew",  padx=10, pady=10)

#add label and Text Box to main_content_frame
main_label = tk.Label(main_content_frame, text="Main Content Area",
                      font=("Helvetiica", 14))
main_text_box = tk.Text(main_content_frame, height=15, width=40)

main_label.grid(row=0, column=0, pady=20)
main_text_box.grid(row=1, column=0, padx=10)



window.mainloop()