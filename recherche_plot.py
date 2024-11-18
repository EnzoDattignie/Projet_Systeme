import sys
from functions import *
import matplotlib.pyplot as plt

longueur = []
intensite = []

for line in sys.stdin :
    l = line.split()
    if len(l) >= 3 :
        print (line.strip())
        if l[0] == 'Clef':
            longueur.append(float(l[2].strip('"')))
        if l[0] == 'Moyenne':
            intensite.append(float(l[2].strip()))
            print('\n')

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
    