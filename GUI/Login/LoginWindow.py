import os
import tkinter as tk
from tkinter import messagebox

from PIL import Image

from DB.Operations.DbActions import DbActions
from GUI.MainWindow.AppGui import AppGui


class LoginWindow(tk.Tk):

    def __init__(self):
        super().__init__()
        self.passwordEntry = None
        self.usernameEntry = None
        self.geometry("1440x1100")
        self.title("Login")
        self.resizable(False, False)
        self.setIcon()
        self.setBackground()
        self.loginDisp()

    # Set background
    def setBackground(self):
        image = tk.PhotoImage(file="GUI/Images/img2.png")
        background = tk.Label(self, image=image)
        background.place(x=0, y=0, relwidth=1, relheight=1)
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

    # Login display TODO change layout
    def loginDisp(self):
        usernameLabel = tk.Label(self, text="Enter your username: ")
        usernameLabel.place(x=0, y=0, anchor=tk.CENTER)
        usernameLabel.pack()

        self.usernameEntry = tk.Entry(self, width=20, bg="yellow")
        self.usernameEntry.place(x=5, y=5, anchor=tk.CENTER)
        self.usernameEntry.pack()

        passwordLabel = tk.Label(self, text="Enter your password: ")
        passwordLabel.place(x=10, y=10, anchor=tk.CENTER)
        passwordLabel.pack()

        self.passwordEntry = tk.Entry(self, width=20, bg="yellow", show="*")
        self.passwordEntry.place(x=15, y=15, anchor=tk.CENTER)
        self.passwordEntry.pack()

        loginButton = tk.Button(self, text="Login", width=18, height=3, command=self.login, bg="yellow")
        loginButton.place(x=20, y=20, anchor=tk.CENTER)
        loginButton.pack()

    # Login function
    def login(self):
        db = DbActions()
        if ((self.usernameEntry.get() == os.environ.get("adName") and self.passwordEntry.get() == os.environ.get("adPass"))
                or db.getUser(self.usernameEntry.get())):
            messagebox.showinfo("Login", "Login successful")
            data = DbActions().getUserPermission(self.usernameEntry.get())
            app = AppGui(data[0], self)
            self.setNotVisible()
            app.run()
        else:
            messagebox.showerror("Error", "Incorrect username or password")
            self.usernameEntry.delete(0, tk.END)
            self.passwordEntry.delete(0, tk.END)

    # Run mainloop
    def run(self):
        self.mainloop()

    # Set window to not visible
    def setNotVisible(self):
        self.withdraw()
