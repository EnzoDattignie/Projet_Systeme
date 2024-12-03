import sys, os
import re

dict = {}

#Fonction retournant True si le string donné peut etre converti en float
def is_number(s):
    flag = False
    res = re.search("(^[-]{0,1}[0-9]*[.]{0,1}[0-9]+$)",s)
    if res :
        flag = True
    res = re.search("(^[-]{0,1}[0-9]+[.]{0,1}[0-9]*$)",s)
    if res :
        flag = True
    return flag


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
        print("Aucun fichier nommé \"{}\" trouvé".format(presence[1]))
    else :
        fd = open(path,"r")
        for ligne in fd :
            x = ligne.strip().split()
            #On vérifie bien que deux nombres sont fournis et que les deux sont des nombres
            if (len(x) == 2 and is_number(x[0]) and is_number(x[1])):
                longueur = float(x[0])
                intensite = float(x[1])
                #On sélectionne comme clef le milieu de la fenetre en mettant dans la meme clef du dictionnaire toutes les longueurs pour lesquelles la division entiere est égale
                #on prend ensuite ce résultat qu'on multiplie par la fenetre et on rajoute une demie fenetre pour que la  clef représente bien le centre de notre fenetre
                key = ((longueur//fenetre)+0.5)*fenetre
                if key in dict.keys() :
                    dict[key].append(intensite)
                else :
                    dict[key] = [intensite]
        fd.close()
    return dict

def is_corrupted(fichier)
    fd=open(fichier,'r')
    l=fd.readlines()
    result=false
    if (len(l)>=0)
        result=true

