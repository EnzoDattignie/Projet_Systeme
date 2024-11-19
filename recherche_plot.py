import sys
from functions import *
import matplotlib.pyplot as plt

longueur = []
intensite = []

<<<<<<< HEAD
if (len(sys.argv) > 1) : #On verifie qu'un argument est donné, sinon on ne peut pas ouvrir le fichier
    longueur,intensite = list_creation(sys.argv[1])
else :
    print("No file indicated, please add a file as an argument")
    
inf=input("Veuillez saisir la première valeur de longueur d'onde en nanomètre de l'intervalle ")
sup=input("Veuillez saisir la seconde valeur de longueur d'onde en nanomètre de l'intervalle ")
=======
for line in sys.stdin :
    l = line.split()
    if len(l) >= 3 :
        print (line.strip())
        if l[0] == 'Clef':
            longueur.append(float(l[2].strip('"')))
        if l[0] == 'Moyenne':
            intensite.append(float(l[2].strip()))
            print('\n')
>>>>>>> 738ebe286c371617c234400b2a8271a879ebd34b

inf = 'null'
sup = 'null'

longueurf=[]
intensitef=[]

if len(sys.argv) >= 3 :
    inf = sys.argv[1].strip() 
    sup = sys.argv[2].strip()

if is_number(inf) and is_number(sup):
    inf_ = float(inf)
    sup_ = float(sup)
    if sup_<inf_:          #inversion de sup et inf si sup<inf
        sup_,inf_=inf_,sup_
else:
    print('Les valeurs rentréées ne sont pas correctes ou inexistantes, plot sur toute la longueur de l\'echantillon')
    inf_ = longueur[minimum(longueur)]
    sup_ = longueur[maximum(longueur)]

for i in range(len(longueur)):  #Creation d'une liste de longueurs d'onde et d'intensités correspondant à l'intervalle demandé
    if inf_ <= longueur[i] <=sup_:        
        longueurf.append(longueur[i])
        intensitef.append(intensite[i])

plt.plot(longueurf,intensitef,label='I(λ)',color='red')
plt.legend()
if len(longueurf)>0:
    plt.show()
else:
    print('Aucune données à afficher sur cet intervalle')
    