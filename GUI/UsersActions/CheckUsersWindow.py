import tkinter as tk
from tkinter import ttk, messagebox

from PIL import Image

from DB.Operations.DbActions import DbActions


class CheckUsersWindow(tk.Toplevel):

    def __init__(self, master):
        super().__init__(master=master)

        self.users = tk.StringVar()
        self.passwordEntry = None
        self.userNameEntry = None
        self.permissionEntry = None
        self.optionVariable = None
        self.confirmButton = None

        self.geometry("1440x1100")
        self.title("Check users")
        self.resizable(False, False)
        self.setIcon()
        self.background()
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

    # option to choose user from db in order to check info about them
    def addUserWidgets(self):
        data = DbActions().getUsers()

        label = tk.Label(self, text="Choose user to check")
        label.pack()

        self.optionVariable = tk.StringVar(self)
        scrollOption = ttk.OptionMenu(self, self.optionVariable, *data, command=self.optionGet)
        scrollOption.config(width=20)
        scrollOption.pack()

        self.confirmButton = tk.Button(self, text="Confirm", command=self.confirm)
        self.confirmButton.config(width=20)
        self.confirmButton.pack()

    def optionGet(self, *args):
        currSelection = self.optionVariable.get()
        self.users.set(currSelection)

    def confirm(self):
        data = DbActions().getUser(self.users.get())
        messagebox.showinfo("User info", "Name: " + str(data[1]) + "\nPermission: " + str(data[0]))

    # Run window
    def run(self):
        self.mainloop()
