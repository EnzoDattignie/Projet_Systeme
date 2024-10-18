import sys

#Simple test de sys.stdin pour récuperer les data print, on peut voir son effet en tappand dans bash "python3 intensite.py Spectre_photoluminescence.txt | python3 test2.py"
for line in sys.stdin :
    print("Info recue : {}".format(line))