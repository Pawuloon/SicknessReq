import tkinter as tk
from PIL import Image


from GUI.AddUser.AddUserWindow import AddUserWindow


# Class for GUI
class AppGui(tk.Toplevel):
    def __init__(self, permission, master):
        super().__init__(master=master)
        self.permission = permission
        self.btn = None
        self.title("Sickness detector")
        self.geometry("1440x1100")
        self.background()
        self.resizable(False, False)
        self.create_widgets()
        self.setIcon()

    # Set background
    def background(self):
        image = tk.PhotoImage(file="GUI/Images/img2.png")
        background = tk.Label(self, image=image)
        background.place(relx=0, rely=0, relwidth=1, relheight=1)
        background.image = image

    # Set icon
    def setIcon(self):

        path = "GUI/Images/img.png"
        icon = Image.open(path)

        if icon.mode != "RGB":
            icon = icon.convert("RGB")

        icoPath = "GUI/Images/imgICO.png"
        icon.save(icoPath, format="ICO")
        self.iconbitmap(icoPath)

    # Set button click function
    def create_widgets(self):
        if self.permission == 3:
            self.btn = tk.Button(self, text="Add user", command=self.addUser)
            self.btn.pack()

    # Add user to db and system
    def addUser(self):
        ad = AddUserWindow(self)
        ad.run()

    # Run mainloop
    def run(self):
        self.mainloop()
