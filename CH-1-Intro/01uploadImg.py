import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

def upload_and_display():
    file_path = filedialog.askopenfilename(
        filetypes=[("Image Files", " *.jpg *.jpeg *.gif *.bmp")]
    )
    if file_path:
        img = Image.open(file_path)
        img = img.resize((300, 300))  

        tk_img = ImageTk.PhotoImage(img)

        image_label.config(image=tk_img)
        image_label.image = tk_img  

# Setup main window
root = tk.Tk()
root.title("Image Uploader")

upload_btn = tk.Button(root, text="Upload Image", command=upload_and_display)
upload_btn.pack(pady=10)

image_label = tk.Label(root)
image_label.pack()

root.mainloop()
