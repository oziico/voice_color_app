import tkinter as tk
from PIL import Image, ImageTk
import os

def show_color_window(color_name):
    image_path = os.path.join("images", f"{color_name}.png")
    if not os.path.exists(image_path):
        print(f"No image found: {image_path}")
        return

    window = tk.Tk()
    window.title(color_name.capitalize())
    window.geometry("400x400")

    img = Image.open(image_path)
    img = img.resize((700, 700))
    tk_img = ImageTk.PhotoImage(img)

    label = tk.Label(window, image=tk_img)
    label.image = tk_img
    label.pack(expand=True)

    text_label = tk.Label(window, text=color_name.capitalize(), font=("Arial", 18))
    text_label.pack(pady=10)

    window.mainloop()
