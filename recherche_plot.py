import sys
from functions import *
import matplotlib.pyplot as plt
import datetime

longueur = []
intensite = []

for line in sys.stdin : #Nous lisons le stdin ligne par ligne pour récuperer les données pipe par intensite.py
    l = line.split()
    if len(l) >= 3 :
        print (line.strip()) #On affiche les lignes rendues invisibles ppar le pipe et on garde en longueur d'onde la clef et en intensité la valeur moyenne sur la fenetre
        if l[0] == "Longueur":
            longueur.append(float(l[2].strip('"')))
        if l[0] == 'Moyenne':
            intensite.append(float(l[2].strip()))
            print('\n')

inf = 'null'
sup = 'null'



if len(sys.argv) >= 3 : #On récupere les longueurs d'ondes min et max voulues fournies par l'utilisateur depuis projet.sh
    inf = sys.argv[1].strip() 
    sup = sys.argv[2].strip()

if is_number(inf) and is_number(sup): #Si ce sont des nombres on les converti en float sinon on prend le min et le max de longueur d'onde
    inf_ = float(inf)
    sup_ = float(sup)
    if sup_<inf_:          #inversion de sup et inf si sup<inf
        sup_,inf_=inf_,sup_
else:
    print('Les valeurs rentrées ne sont pas correctes ou inexistantes, plot sur toute la longueur de l\'echantillon')
    if (len(longueur) > 0) : #Evite juste une erreur si l'échantillon est vide
        inf_ = longueur[minimum(longueur)]
        sup_ = longueur[maximum(longueur)]
    else :
        inf_ = 0
        sup_ = 0

#Ces listes seront les listes réelles entre les deux valeurs de longueur d'onde indiquées par l'utilisateur
longueurf=[] 
intensitef=[]
for i in range(len(longueur)):  #Creation d'une liste de longueurs d'onde et d'intensités correspondant à l'intervalle demandé
    if inf_ <= longueur[i] <=sup_:        
        longueurf.append(longueur[i])
        intensitef.append(intensite[i])

#Normalisation de l'intensité

if len(intensite) > 0 :
    Imax=intensite[maximum(intensite)]
else :
    Imax = 0
intensitef_normalisé=[]
for i in range(len(intensitef)):
    intensitef_normalisé.append(intensitef[i]/Imax)

filename = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
plt.plot(longueurf,intensitef_normalisé,label='I(λ)',color='red')
plt.ylim(-0.10,1.10)
plt.legend()
plt.xlabel("Longueur d'onde (λ)")
plt.ylabel("Intensité (I)")
plt.title("Graphique représentant l'intensité en fonction de la longueur d'onde")

if len(longueurf)>0: #On verifie que les listes sont remplies avant de plot
    if sys.argv[3] == 'y':
        filename = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
        plt.savefig(filename)
    plt.show()
else:
    print('Aucune données à afficher sur cet intervalle')

    
