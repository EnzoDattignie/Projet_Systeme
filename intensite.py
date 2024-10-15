fd = open("Spectre_photoluminescence.txt","r")
for ligne in fd :
    x = ligne.strip().split()
    if (x[0].isdigit()) :
        print (x[0])
fd.close()
print("travail terminé")