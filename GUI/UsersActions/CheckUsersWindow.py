import tkinter as tk
from tkinter import ttk

from PIL import Image

from DB.Operations.DbActions import DbActions


class CheckUsersWindow(tk.Toplevel):

    def __init__(self, master):
        super().__init__(master=master)
        self.users = None
        self.geometry("1440x1100")
        self.title("Check users")
        self.resizable(False, False)
        self.setIcon()
        self.background()
        self.passwordEntry = None
        self.userNameEntry = None
        self.permissionEntry = None

        self.addUserWidgets()

    def background(self):
        image = tk.PhotoImage(file="GUI/Images/img2.png")
        background = tk.Label(self, image=image)
        background.place(relx=0, rely=0, relwidth=1, relheight=1)
        background.image = image

    def setIcon(self):
        path = "GUI/Images/img.png"
        icon = Image.open(path)

        if icon.mode != "RGB":
            icon = icon.convert("RGB")

        icoPath = "GUI/Images/imgICO.png"
        icon.save(icoPath, format="ICO")
        self.iconbitmap(icoPath)

    # TODO: add option to choose user from db in order to check info about them
    # option to choose user from db in order to check info about them
    def addUserWidgets(self):
        label = tk.Label(self, text="Choose user to check")
        scrollOption = ttk.OptionMenu(self, *self.users, command=self.getUsers())

    def getUsers(self):
        db = DbActions()
        self.users = db.getUsers()
        return self.users
