import tkinter as tk
from PIL import Image

from GUI.UsersActions.AddUserWindow import AddUserWindow
from GUI.SicknessInfo.SicknessWindow import SicknessWindow
from GUI.UsersActions.CheckUsersWindow import CheckUsersWindow


# Class for GUI
class AppGui(tk.Toplevel):
    def __init__(self, permission, master):
        super().__init__(master=master)
        self.btn3 = None
        self.protocol("WM_DELETE_WINDOW", self.master.destroy)
        self.btn2 = None
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
            self.btn2 = tk.Button(self, text="Sicknesses", command=self.sicknessesAccess)
            self.btn2.pack()
            self.btn3 = tk.Button(self, text="Check users", command=self.checkUsers)
            self.btn3.pack()

    def checkUsers(self):
        us = CheckUsersWindow(self)
        us.run()

    # Add user to db and system
    def addUser(self):
        ad = AddUserWindow(self)
        ad.run()

    # Check sicknesses
    def sicknessesAccess(self):
        sc = SicknessWindow(self)
        sc.run()

    # Run mainloop
    def run(self):
        self.mainloop()
