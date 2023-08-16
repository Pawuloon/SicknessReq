import tkinter as tk
from PIL import Image


# Class for GUI
class AppGui(tk.Tk):
    def __init__(self):
        super().__init__()
        self.btn_click = None
        self.btn = None
        self.title("Sickness detector")
        self.geometry("500x500")
        self.resizable(False, False)
        self.create_widgets()
        self.background("white")
        self.set_icon()

    # TODO change it into picture later
    # Set background
    def background(self, color):
        self.configure(bg=color)

    # Set icon
    def set_icon(self):
        path = "GUI/Images/img.png"
        icon = Image.open(path)
        icoPath = "GUI/Images/imgICO.png"
        icon.save(icoPath, format="ICO")
        self.iconbitmap(icoPath)

    # Set button click function
    def create_widgets(self):
        self.btn = tk.Button(self, text="Click me!", command=self.btn_click)
        self.btn.pack()

    # Run mainloop
    def run(self):
        self.mainloop()
