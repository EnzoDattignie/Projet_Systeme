import sys
import matplotlib.pyplot as plt

from functions import *

if (len(sys.argv) > 1) : #On verifie qu'un argument est donné, sinon on ne peut pas ouvrir le fichier
    longueur,intensite = list_creation(sys.argv[1])
else :
    print("No file indicated, please add a file as an argument")
inf=input("Veuillez saisir la première valeur de longueur d'onde de l'intervalle ")
sup=input("Veuillez saisir la seconde valeur de longueur d'onde de l'intervalle ")

def fenetre():             #pas utile au final
    if not is_number(inf) and not is_number(sup):
        print('valeur non valable')
    else:
        fenetre=abs(float(sup)-float(inf))
    return fenetre

longueurf=[]
intensitef=[]
if is_number(inf) and is_number(sup):
    inf_ = float(inf)
    sup_ = float(sup)
    if sup_<inf_:          #inversion de sup et inf si sup<inf
        sup_,inf_=inf_,sup_
    for i in range(len(longueur)):  #Creation d'une liste de longueurs d'onde et d'intensités correspondant à l'intervalle demandé
        if inf_ <= longueur[i] <=sup_:        
            longueurf.append(longueur[i])
            intensitef.append(intensite[i])
else:
    print('Les valeurs rentrées ne sont pas des nombres')


plt.plot(longueurf,intensitef,label='I(λ)',color='red')
plt.legend()
if len(longueurf)>0:
    plt.show()
else:
    print('Les valeurs rentrées ne correspondent pas aux données')
