import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

window = tk.Tk()
window.title("Browe Photo")
window.geometry("500x400")

def open_photo():
    file_path = filedialog.askopenfilename(
        title="Select an Image",
        filetypes=[("Image files", "*.png *.jpg")]
    )
    
    if file_path:
        image = Image.open(file_path)
        image = image.resize((400, 300))
        
        widget_img = ImageTk.PhotoImage(image)
        imgLabel.config(image=widget_img)
        imgLabel.image = widget_img


uploadBtn = tk.Button(window, text="Upload Photo", command=open_photo)
uploadBtn.pack()

imgLabel = tk.Label(window)
imgLabel.pack()

window.mainloop()