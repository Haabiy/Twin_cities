from unidecode import unidecode
from __selected_data import targetlst
# NB: check the encoding here in the lst_france
lst_belgium = ["Kortrijk"]
lst_finland = ["Helsinki"]
lst_france = ["Montpellier", "Belfort", "Vannes", "Paris", "Avignon", "Saint-Etienne" , "Strasbourg", "Carcassonne", "Landerneau", "Epinal", "Nice", "Saint-Brieuc", "Montelimar"]
twin_belgium, twin_finland, twin_france= ([] for i in range(3))
def print_sister_cities(x,ind_,y,z):
    print("_________________...", targetlst[ind_], "..._________________")
    for cities in range(0, len(x)):
        for twins in range(0, len(y)):
            if (unidecode(x[cities]) == y[twins]):
                print(cities + 1, x[cities])
                z.append(x[cities])
            else:
                pass


