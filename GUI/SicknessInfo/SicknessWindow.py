import tkinter as tk
from PIL import Image
from WebScraper.WikiScraper import WikiScraper


class SicknessWindow(tk.Toplevel):

    def __init__(self, master):
        super().__init__(master=master)
        self.title("Sickness info")
        self.geometry("500x400")
        self.resizable(True, True)
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

    # Sickness search from wiki
    def sicknessWidgets(self):
        # Sickness entry
        self.sicknessEntry = tk.Entry(self, font=("Arial", 12))
        self.sicknessEntry.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.1)

        # Search button
        searchButton = tk.Button(self, text="Search", font=("Arial", 12), command=self.searchSickness)
        searchButton.place(relx=0.1, rely=0.2, relwidth=0.8, relheight=0.1)

    # Search sickness from wiki with scrollbar
    def searchSickness(self):
        name = self.sicknessEntry.get()
        Wik = WikiScraper(name)
        title = Wik.getWikiTitle()
        wiki = Wik.getWiki()

        # Sickness info entry
        self.sicknessInfoEntry = tk.Text(self, font=("Arial", 12))
        self.sicknessInfoEntry.place(relx=0.1, rely=0.3, relwidth=0.8, relheight=0.6)
        self.sicknessInfoEntry.insert(tk.END, title + "\n\n" + wiki)

        # Scrollbar
        scrollbar = tk.Scrollbar(self)
        scrollbar.place(relx=0.9, rely=0.3, relwidth=0.1, relheight=0.6)
        scrollbar.config(command=self.sicknessInfoEntry.yview)
        self.sicknessInfoEntry.config(yscrollcommand=scrollbar.set)

        self.sicknessEntry.delete(0, tk.END)
    def run(self):
        self.mainloop()
