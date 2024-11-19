import sys
from functions import *
import matplotlib.pyplot as plt

longueur = []
intensite = []

for line in sys.stdin : #Nous lisons le stdin ligne par ligne pour récuperer les données pipe par intensite.py
    l = line.split()
    if len(l) >= 3 :
        print (line.strip()) #On affiche les lignes rendues invisibles ppar le pipe et on garde en longueur d'onde la clef et en intensité la valeur moyenne sur la fenetre
        if l[0] == 'Clef':
            longueur.append(float(l[2].strip('"')))
        if l[0] == 'Moyenne':
            intensite.append(float(l[2].strip()))
            print('\n')

inf = 'null'
sup = 'null'

if len(sys.argv) >= 3 : #On récupere les longueurs d'ondes min et max voulues fournies par l'utilisateur depuis projet.sh
    inf = sys.argv[1].strip() 
    sup = sys.argv[2].strip()

if is_number(inf) and is_number(sup): #Si ce sont des nombres on les converti en float sinonn on prend le min et le max de longueur d'onde
    inf_ = float(inf)
    sup_ = float(sup)
    if sup_<inf_:          #inversion de sup et inf si sup<inf
        sup_,inf_=inf_,sup_
else:
    print('Les valeurs rentréées ne sont pas correctes ou inexistantes, plot sur toute la longueur de l\'echantillon')
    inf_ = longueur[minimum(longueur)]
    sup_ = longueur[maximum(longueur)]

#Ces listes seront les listes réelles entre les deux valeurs de longueur d'onde indiquées par l'utilisateur
longueurf=[] 
intensitef=[]
Imax=intensite[maximum(intensite)]
for i in range(len(longueur)):  #Creation d'une liste de longueurs d'onde et d'intensités correspondant à l'intervalle demandé
    if inf_ <= longueur[i] <=sup_:        
        longueurf.append(longueur[i])
        intensitef.append(intensite[i]/Imax) #Normalisation de l'intensité



    
plt.plot(longueurf,intensitef,label='I(λ)',color='red')
plt.legend()
if len(longueurf)>0: #On verifie que les listes sont remplies avant de plot
    plt.show()
else:
    print('Aucune données à afficher sur cet intervalle')
    
