import tkinter as tk
from tkinter import PhotoImage

window = tk.Tk()
window.title("Photo Image")

imagePath = PhotoImage(file='D:\PyGUI\CH-2-Image-Widget\img-1.png')

imgLabel = tk.Label(window, image=imagePath)
imgLabel.pack()

window.mainloop()