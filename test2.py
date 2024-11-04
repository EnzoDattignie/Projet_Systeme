import sys
import matplotlib.pyplot as plt
dic = {}

#Simple test de sys.stdin pour récuperer les data print, on peut voir son effet en tappand dans bash "python3 intensite.py Spectre_photoluminescence.txt | python3 test2.py"
for line in sys.stdin :
    l = line.split()
    if l[0] == "Clef" :
        key = float(l[2].strip('"'))
    if l[0] == "Moyenne" :
        dic[key] = float(l[2])
        
wavelength = []
intensity = []
for key in dic :
    wavelength.append(key)
    intensity.append(dic[key])

print (wavelength)
print (intensity)

