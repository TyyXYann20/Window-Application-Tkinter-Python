import tkinter as tk
from tkinter import PhotoImage

window = tk.Tk()
window.title("Photo Image")

imagePath = PhotoImage(file='D:\PyGUI\CH-2-Image-Widget\img-1.png')
imagePath.write("crop-2.png", format="png", from_coords=(0, 370, 370, 0))


window.mainloop()