import sys
from functions import *
dict = {}


fenetre = 10
if len(sys.argv) > 2: #On verifie qu'une fenetre est bien donnée et que c'est bien un nombre, sinon on la laisse a 10
    if is_number(sys.argv[2].strip()) :
        fenetre = float(sys.argv[2])
    else :
        print("Erreur, fenetre paramétrée a 10nm")

if (len(sys.argv) > 1) : #On verifie qu'un argument est donné, sinon on ne peut pas ouvrir le fichier
    dict = dict_creation(sys.argv[1].strip(),fenetre)
else :
    print("Pas de fichier indiqué, merci d'indiquer un fichier en argument")

#Retour de toutes les données demandées
for key in dict :
    dict[key] = sort_list(dict[key])
    print ("Longueur : \"{}\"".format(key))
    print ("Nb de données : {}".format(len(dict[key])))
    print ("Min : {}".format(dict[key][minimum(dict[key])]))
    print ("Max : {}".format(dict[key][maximum(dict[key])]))
    print ("Moyenne : {}".format(average(dict[key])))
    print ()
