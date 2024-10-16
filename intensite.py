
#Fonction retournant True si le string donné peut etre converti en float
def is_number(s):
    fpoint = False
    res = True
    i = 0
    if (len(s)==0):
        res = False
    if (s[0].isdigit() == False) :
        res = False
    while ((i < len(s)) and (res == True)) :
        if (s[i].isdigit() == False):
            if (s[i] == "." and fpoint == False):
                fpoint = True
            else :
                res = False
        i = i+1
    return res


intensite = []
longueur = []

fd = open("Spectre_photoluminescence.txt","r")
for ligne in fd :
    x = ligne.strip().split()
    #On vérifie bien que deux nombres sont fournis et que les deux sont des nombres
    if (len(x) == 2 and is_number(x[0]) and is_number(x[1])):
        longueur.append(float(x[0]))
        intensite.append(float(x[1]))
fd.close()

print(longueur)
print(intensite)
