
#Fonction retournant True si le string donné peut etre converti en float
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

fd = open("Spectre_photoluminescence.txt","r")
for ligne in fd :
    x = ligne.strip().split()
    #On vérifie bien que deux nombres sont fournis et que les deux sont des nombres
    if (len(x) == 2 and is_number(x[0]) and is_number(x[1])):
        print (x[0])
fd.close()
print("travail terminé")