from time import sleep
from __sign__in import signin
from __selected_data import _data, selected_url
from __cities import cities, all_cities_Belgium, all_cities_Finland, all_cities_France
from __print import print_all_cities
from __print_sister_cities import print_sister_cities, lst_belgium, lst_finland, lst_france, twin_belgium, twin_finland, twin_france
from bs4 import BeautifulSoup
from __sign__in import driver
signin()
_data()
for t in range(0, len(selected_url)):
    cities(t)
    sleep(1)

#print_all_cities(all_cities_Belgium, 0)
#print_all_cities(all_cities_Finland, 1)
#print_all_cities(all_cities_France, 2)


#print_sister_cities(all_cities_Belgium, 0, lst_belgium, twin_belgium)
#print_sister_cities(all_cities_Finland, 1, lst_finland, twin_finland)
#print_sister_cities(all_cities_France, 2, lst_france, twin_france)

print("_____________...Main targets...______________")
soup = BeautifulSoup(driver.page_source, "html.parser")
body = soup.find("body")
all_c = []
all_s = []
for tt in range(0, 5):
    for div in body.find_all("div", {"class": "mw-parser-output"}):
        b = div.find_all("b")[tt].text.strip()
        all_c.append(b)
        for div in body.find_all("div", {"class": "div-col"})[tt]:
            for ff in range(0, 10):
                try:
                    _country = div.find_all("li")[ff].text.strip()
                    all_s.append(_country)
                except Exception:
                    pass
print("________________________________")
for rr in range(0, len(all_c)):
    print(rr+1, all_c[rr])
print("________________________________")
for rr in range(0, len(all_s)):
    print(rr+1, all_s[rr])


sleep(1000)