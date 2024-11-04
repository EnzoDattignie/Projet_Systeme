import sys
from functions import *
dic = {}

fenetre = 10

if len(sys.argv) > 2:
    if is_number(sys.argv[2]) :
        fenetre = float(sys.argv[2])
    else :

#Retour de toutes les données demandées
for key in dict :
    dict[key] = sort_list(dict[key])
    print ("Clef : \"{}\"".format(key))
    print ("Nb de données : {}".format(len(dict[key])))
    print ("Min : {}".format(minimum(dict[key])))
    print ("Max : {}".format(maximum(dict[key])))
    print ("Moyenne : {}".format(average(dict[key])))