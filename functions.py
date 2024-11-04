import sys, os

dict = {}

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

#Programme retournant la moyenne d'une liste
def average(l):
    res = 0
    for elmt in l :
        res = res + elmt
    return (res/len(l))

#Fonction dont le but est de trier une liste comme demandé dans les consignes pour les intensités
def sort_list(list) :
    l = list
    res = []
    while len(l) > 0 :
        index_min = minimum(l)
        res.append(l[index_min])
        del l[index_min]
    return res

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

def dict_creation (path,fenetre):
    dict = {}
    presence = file_here(path)
    if presence[0] == False :
        print("No file named \"{}\" found".format(presence[1]))
    else :
        fd = open(path,"r")
        for ligne in fd :
            x = ligne.strip().split()
            #On vérifie bien que deux nombres sont fournis et que les deux sont des nombres
            if (len(x) == 2 and is_number(x[0]) and is_number(x[1])):
                longueur = float(x[0])
                intensite = float(x[1])
                #On sélectionne la clef sous la forme [limite_basse-Limite_haute[ et ensuite on initialise la liste des intensités si elle n'existe pas, on append si elle existe
                key = "["+str((longueur//fenetre)*fenetre) +"-" +str((longueur//fenetre+1)*fenetre)+"["
                if key in dict.keys() :
                    dict[key].append(intensite)
                else :
                    dict[key] = [intensite]
        fd.close()
    return dict

def list_creation (path):
    longueur = []
    intensite = []
    presence = file_here(path)
    if presence[0] == False :
        print("No file named \"{}\" found".format(presence[1]))
    else :
        fd = open(path,"r")
        for ligne in fd :
            x = ligne.strip().split()
            #On vérifie bien que deux nombres sont fournis et que les deux sont des nombres
            if (len(x) == 2 and is_number(x[0]) and is_number(x[1])):
                longueur.append(float(x[0]))
                intensite.append(float(x[1]))
        fd.close()
    return longueur,intensite