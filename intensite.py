import sys
from functions import *
dict = {}

if not(is_corrupted(sys.argv[0],sys.argv[0])):
    window = 10
    if len(sys.argv) > 2: #We check that a window is provided and that it's a number, otherwise we let it at 10nm
        if is_number(sys.argv[2].strip()) :
            window = float(sys.argv[2])
        else :
            print("Error, window automatically set to 10nm")

    if (len(sys.argv) > 1) : #We verify that an argument is given, otherwise wwe can't open the file
        dict = dict_creation(sys.argv[1].strip(),window)
    else :
        print("No file provided, Please add a file as an argument")

    #Printing all important value
    for key in dict :
        dict[key] = sort_list(dict[key])
        print ("Wavelength : \"{}\"".format(key))
        print ("Number of Points : {}".format(len(dict[key])))
        print ("Min : {}".format(dict[key][minimum(dict[key])]))
        print ("Max : {}".format(dict[key][maximum(dict[key])]))
        print ("Average : {}".format(average(dict[key])))
        print ()
