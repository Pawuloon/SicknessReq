from GUI.Login.LoginWindow import LoginWindow
from WebScraper.WikiScraper import WikiScraper


class Main:
    if __name__ == "__main__":
#        login = LoginWindow()
#        login.run()
        web = WikiScraper("Bacteria")
        print(web.getWikiTitle())
        print(web.getWiki())