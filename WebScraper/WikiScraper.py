from bs4 import BeautifulSoup
import requests


class WikiScraper:
    def __init__(self, url):
        self.url = "https://en.wikipedia.org/wiki/" + url
        self.page = requests.get(self.url)
        self.soup = BeautifulSoup(self.page.content, 'html.parser')

    # Get title of wiki page
    def getWikiTitle(self):
        return self.soup.title.string

    # Get content from wiki page
    def getWiki(self):
        return self.soup.find(id="bodyContent").getText()

    # Get additional links from wiki page
    def getWikiLinks(self):
        return self.soup.find_all('a')
