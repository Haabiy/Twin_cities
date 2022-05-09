from time import sleep
from __info import info, no_of_countries

targetlst = ["Belgium", "Finland", "France"]
selected_countries, selected_url = ([] for i in range(2))
def _data():
    xx = info()
    xx.storecountries()
    xx.countries_url()
    y = [15, 22, 37]
    xx.eexceptions(y[0], y[1], y[2])
    print("__________________...Total countries...___________________")
    sleep(1)
    #print(len(xx.countries))
    for tt in range(0, no_of_countries):
        print(tt+1, xx.countries[tt])
        for jj in range(0, len(targetlst)):
            try:
                if (xx.countries[tt]==targetlst[jj]):
                    selected_countries.append(xx.countries[tt])
                    selected_url.append("https://en.wikipedia.org" + xx.storelinks[tt])
                else:
                    pass
            except Exception:
                pass