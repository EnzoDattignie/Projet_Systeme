import sys
from functions import *

if (len(sys.argv) > 1) : #On verifie qu'un argument est donné, sinon on ne peut pas ouvrir le fichier
    longueur,intensite = list_creation(sys.argv[1])
else :
    print("No file indicated, please add a file as an argument")

print (longueur)
print (intensite)