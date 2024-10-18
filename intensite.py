import sys, os


#Fonction retournant True si le string donné peut etre converti en float
def is_number(s) :
    fpoint = False #Ce flag vérifie que le point est passé ou non, il est set a True si il voit un point et si il voit de nouveau un point le résultat final est false, un float ne possede qu'un seul point
    res = True
    i = 1
    if (len(s)==0):
        res = False
    else :
        #un string peut etre converti en float si il commence par un chiffre, un moins, ou un point
        if s[0].isdigit() or s[0] == "-" or s[0] == "." :
            if s[0] == ".":
                fpoint = True
            while ((i < len(s)) and (res == True)) :
                if (s[i].isdigit() == False):
                    if (s[i] == "." and fpoint == False):
                        fpoint = True
                    else :
                        res = False
                i = i+1
        else :
            res = False
    return res


intensite = []
longueur = []

#Programme retournant l'index de la valeur minimale d'une liste
def minimum(l) :
    res = l[0]
    index = 0
    for i in range (0,len(l)):
        if (l[i] < res):
            res = l[i]
            index = i
    return index

def maximum(l) :
    res = l[0]
    index = 0
    for i in range (0,len(l)):
        if (l[i] > res):
            res = l[i]
            index = i
    return index

#Programme vérifiant que le chemin fourni mene bien a un fichier existant qui prend en compte tout type de chemin
def file_here(path):
    presence = False
    if (path[0] == "/" or path[0] == "." or path[0] == "~"):#On est face a un chemin absolu ou relatif
        path = path.split("/")
        file = path[len(path)-1]
        dir = ""
        for i in range (0, len(path)-1):
            dir = dir+path[i]+"/"
        fichiers = os.listdir(dir)
    else : #On est dans le cas d'un nom de fichier
        fichiers = os.listdir("./")
        file = path
    for f in fichiers : #vérification que le fichier existe bien a l'endroit indiqué
        if (f == file) :
            presence = True
    return presence,file

if (len(sys.argv) > 1) : #On verifie qu'un argument est donné, sinon on ne peut pas ouvrir le fichier
    presence = file_here(sys.argv[1])
    if presence[0] == False :
        print("No file named \"{}\" found".format(presence[1]))
    else :
        fd = open(sys.argv[1],"r")
        for ligne in fd :
            x = ligne.strip().split()
            #On vérifie bien que deux nombres sont fournis et que les deux sont des nombres
            if (len(x) == 2 and is_number(x[0]) and is_number(x[1])):
                longueur.append(float(x[0]))
                intensite.append(float(x[1]))
        fd.close()
        maxi = maximum(intensite)
        mini = minimum(intensite)
        print("intensite max = {} , pour une longueur d'onde de {}".format(intensite[maxi],longueur[maxi]))
        print("intensite min = {} , pour une longueur d'onde de {}".format(intensite[mini],longueur[mini]))
else :
    print("No file indicated, please add a file as an argument")


