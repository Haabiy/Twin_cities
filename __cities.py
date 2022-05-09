from bs4 import BeautifulSoup
from __sign__in import driver
from __selected_data import selected_url

all_cities_Belgium, all_cities_Finland, all_cities_France = ([] for i in range(3))
def cities(t):
    driver.get(selected_url[t])
    _soup = BeautifulSoup(driver.page_source, "html.parser")
    for _body in _soup.find_all("body"):
        i = 0
        while (i >= 0):
            p = _body.find_all("b")[i].text.strip()
            i = i + 1
            if (p == "^"):
                break
            else:
                pass
            if(t==0):
                all_cities_Belgium.append(p)
            elif(t==1):
                all_cities_Finland.append(p)
            elif(t==2):
                all_cities_France.append(p)
            #print(i, ".", p)


