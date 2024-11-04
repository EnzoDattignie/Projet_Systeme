import sys
from functions import *
dict = {}

fenetre = 10

if len(sys.argv) > 2:
    if is_number(sys.argv[2]) :
        fenetre = float(sys.argv[2])
    else :
        print("Error, window set to 10nm automatically")

if (len(sys.argv) > 1) : #On verifie qu'un argument est donné, sinon on ne peut pas ouvrir le fichier
    dict = dict_creation(sys.argv[1],fenetre)
else :
    print("No file indicated, please add a file as an argument")

#Retour de toutes les données demandées
for key in dict :
    dict[key] = sort_list(dict[key])
    print ("Clef : \"{}\"".format(key))
    print ("Nb de données : {}".format(len(dict[key])))
    print ("Min : {}".format(minimum(dict[key])))
    print ("Max : {}".format(maximum(dict[key])))
    print ("Moyenne : {}".format(average(dict[key])))