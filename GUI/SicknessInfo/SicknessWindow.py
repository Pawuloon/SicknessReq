import tkinter as tk
from PIL import Image


class SicknessWindow(tk.Toplevel):

    def __init__(self):
        super().__init__()
        self.title("Sickness info")
        self.geometry("500x400")
        self.resizable(False, False)
        self.setIcon()
        self.background()
        self.sicknessEntry = None
        self.sicknessInfoEntry = None
        self.sicknessWidgets()

    # Set icon
    def setIcon(self):
        path = "GUI/Images/img.png"
        icon = Image.open(path)

        if icon.mode != "RGB":
            icon = icon.convert("RGB")

        icoPath = "GUI/Images/imgICO.png"
        icon.save(icoPath, format="ICO")
        self.iconbitmap(icoPath)

    # Set background
    def background(self):
        image = tk.PhotoImage(file="GUI/Images/img2.png")
        background = tk.Label(self, image=image)
        background.place(relx=0, rely=0, relwidth=1, relheight=1)
        background.image = image

    # Sickness widgets
    def sicknessWidgets(self):
        pass

