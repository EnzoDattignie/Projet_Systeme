from functions import is_corrupted,is_number

path = "/Users/ahmed/Documents/M1/Systeme/Projet_Systeme"
fichier = "Spectre_photoluminescence.txt"
#fichier = "empty_file.txt"

if is_corrupted(path, fichier):
    print("Le fichier est corrompu.")
else:
    print("Le fichier est valide.")


#print(is_not_corrupted("Spectre_photoluminescence.txt",Spectre_photoluminescence.txt))
#print(is_number('1022.71'))