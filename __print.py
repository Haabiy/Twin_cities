from __selected_data import targetlst
def print_all_cities(x,ind_):
    print("_________________...", targetlst[ind_], "..._________________")
    for cities in range(0, len(x)):
        print(cities +1, ".", x[cities])

