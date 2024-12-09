from queue import Full
import sys
from functions import *
import matplotlib.pyplot as plt
import datetime
import select

#Vérification si des données sont disponibles sur stdin
flag = select.select([sys.stdin], [], [], 1)[0]  # Attend jusqu'à 1 seconde

#Initialisation des listes pour stocker les données
longueur = []
intensite = []

if flag:      #Lecture des données depuis stdin
    stdin_data=list(sys.stdin)
    if len(stdin_data) == 0:
        print("Le fichier est corrumpu")
        sys.exit(1)
    
    if sys.argv[4] == "n" :
        for line in stdin_data : #Nous lisons le stdin ligne par ligne pour récuperer les données pipe par intensite.py
            l = line.split()
            if len(l) >= 3 :
                print (line.strip()) #On affiche les lignes rendues invisibles par le pipe et on garde en longueur d'onde la clef et en intensité la valeur moyenne sur la fenetre
                if l[0] == "Longueur":
                    longueur.append(float(l[2].strip('"')))
                if l[0] == 'Moyenne':
                    intensite.append(float(l[2].strip()))
                    print('\n')

else:          #Lecture des données depuis temp.txt
    with open("temp.txt","r") as temp:
        for l in temp :
            line = l.split()
            longueur.append(float(line[0]))
            intensite.append(float(line[1]))     


inf = sys.argv[1].strip() 
sup = sys.argv[2].strip()

if is_number(inf) and is_number(sup): #Si ce sont des nombres on les converti en float sinon on prend le min et le max de longueur d'onde
    inf_ = float(inf)
    sup_ = float(sup)
    if sup_<inf_:          #inversion de sup et inf si sup<inf
        sup_,inf_=inf_,sup_
else:
    print('Valeurs non renseignées sur les bornes, plot sur toute la longueur de l\'echantillon')
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

with open("temp.txt","w") as temp :
    for i in range(0,len(intensite)) :
        temp.write("{}\t{}\n".format(longueur[i],intensite[i]))

if len(longueurf)>0: #On verifie que les listes sont remplies avant de plot
    if sys.argv[3] == 'y':
        filename = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
        with open(filename+"_save.txt",'w') as save :
            for i in range (0,len(intensitef_normalisé)) :
                save.write("{}\t{}\n".format(longueurf[i],intensitef_normalisé[i]))
        plt.savefig(filename)
    plt.show()
else:
    print('Aucune données à afficher sur cet intervalle')
