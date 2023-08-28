import tkinter as tk
from tkinter import messagebox

from PIL import Image

from DB.Operations.DbActions import DbActions


class AddUserWindow(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master=master)
        self.geometry("500x400")
        self.title("Add user")
        self.resizable(False, False)
        self.setIcon()
        self.background()
        self.passwordEntry = None
        self.userNameEntry = None
        self.permissionEntry = None

        self.addUserWidgets()

    # set background
    def background(self):
        image = tk.PhotoImage(file="GUI/Images/img2.png")
        background = tk.Label(self, image=image)
        background.place(relx=0, rely=0, relwidth=1, relheight=1)
        background.image = image

    # set icon
    def setIcon(self):
        path = "GUI/Images/img.png"
        icon = Image.open(path)

        if icon.mode != "RGB":
            icon = icon.convert("RGB")

        icoPath = "GUI/Images/imgICO.png"
        icon.save(icoPath, format="ICO")
        self.iconbitmap(icoPath)

    # Add user widgets
    def addUserWidgets(self):

        userNameLabel = tk.Label(self, text="Enter user username: ")
        userNameLabel.place(x=0, y=0, anchor=tk.CENTER)
        userNameLabel.pack()

        self.userNameEntry = tk.Entry(self, width=20, bg="yellow")
        self.userNameEntry.place(x=5, y=5, anchor=tk.CENTER)
        self.userNameEntry.pack()

        passwordLabel = tk.Label(self, text="Enter user password: ")
        passwordLabel.place(x=10, y=10, anchor=tk.CENTER)
        passwordLabel.pack()

        self.passwordEntry = tk.Entry(self, width=20, bg="yellow", show="*")
        self.passwordEntry.place(x=15, y=15, anchor=tk.CENTER)
        self.passwordEntry.pack()

        permissionLabel = tk.Label(self, text="Enter user permission: ")
        permissionLabel.place(x=20, y=20, anchor=tk.CENTER)
        permissionLabel.pack()

        self.permissionEntry = tk.Entry(self, width=20, bg="yellow")
        self.permissionEntry.place(x=25, y=25, anchor=tk.CENTER)
        self.permissionEntry.pack()

        buttonAddUser = tk.Button(self, text="Add user", width=30, height=3, command=self.addUser, bg="yellow")
        buttonAddUser.place(x=30, y=30, anchor=tk.CENTER)
        buttonAddUser.pack()

    # Add user to db and system
    def addUser(self):
        db = DbActions()
        if self.userNameEntry is not None and self.passwordEntry is not None and self.permissionEntry is not None:
            db.insertUser(str(self.userNameEntry.get()), self.passwordEntry.get(), self.permissionEntry.get())
            messagebox.showinfo("Success", "User added successfully")
        else:
            messagebox.showerror("Error", "Invalid input")

    def run(self):
        self.mainloop()
