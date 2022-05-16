from bs4 import BeautifulSoup
from __sign__in import driver
from unidecode import unidecode
no_of_countries = 47
class info():
    def __init__(self):
        # Initializing common parameters
        self.countries, self.storelinks = ([] for i in range(2))
        self.soup = BeautifulSoup(driver.page_source, "html.parser")
        self.body = self.soup.find("body")
    def storecountries(self):
        for div in self.body.find_all("div", {"class": "mw-parser-output"}):
            for i in range(0, no_of_countries):
                # unidecode to get rid of uncommon letters(outside of the English letters)
                names = unidecode(div.find_all("span", {"class": "mw-headline"})[i].text.strip())
                self.countries.append(names)
                #print(names)

    def countries_url(self):
        for i in range(0, no_of_countries):
            for href in self.body.find_all("div", {"class": "hatnote navigation-not-searchable"}):
                try:
                    a = href.find("a", href=True)
                    if a.text:
                        self.storelinks.append(a['href'])
                        #print(a['href'])
                except Exception:
                    pass
    # we have 3 countries as exceptions
    def eexceptions(self, a, b,c):
        self.storelinks.insert(a, "None")
        self.storelinks.insert(b, "None")
        self.storelinks.insert(c, "None")
