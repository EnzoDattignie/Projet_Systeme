import sys, os
import re

dict = {}

#Function returning true if the string can be converted into a float
def is_number(s):
    flag = False
    res = re.search("(^[-]{0,1}[0-9]*[.]{0,1}[0-9]+$)",s)
    if res :
        flag = True
    res = re.search("(^[-]{0,1}[0-9]+[.]{0,1}[0-9]*$)",s)
    if res :
        flag = True
    return flag


#Functions giving respectively the index of the minimal and maximal value from a list
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

#Returns the average of a list
def average(l):
    res = 0
    for elmt in l :
        res = res + elmt
    return (res/len(l))

#Function sorting a list
def sort_list(list) :
    l = list
    res = []
    while len(l) > 0 :
        index_min = minimum(l)
        res.append(l[index_min])
        del l[index_min]
    return res

#Function verifying that a given path is a pointing to an existing file
def file_here(path):
    presence = False
    if (path[0] == "/" or path[0] == "." or path[0] == "~"):#We have an absolute or relative path
        path = path.split("/")
        file = path[len(path)-1]
        dir = ""
        for i in range (0, len(path)-1):
            dir = dir+path[i]+"/"
        fichiers = os.listdir(dir)
    else : #We just have a filename
        fichiers = os.listdir("./")
        file = path
    for f in fichiers : #Check that the givenfile exists
        if (f == file) :
            presence = True
    return presence,file

#Function creating a full dictionnary from a text file and a window
def dict_creation (path,window):
    dict = {}
    presence = file_here(path)
    if presence[0] == False :
        print("No file named \"{}\" found".format(presence[1]))
    else :
        fd = open(path,"r")
        for line in fd :
            x = line.strip().split()
            #We check that two strings are given and that they are numbers
            if (len(x) == 2 and is_number(x[0]) and is_number(x[1])):
                wavelength = float(x[0])
                intensity = float(x[1])
                #We use as a key the middle of the window, we determine the key by making an integer division of the wavelength by the window
                #we then take this result that we multiply by the window and add half a window so the key actually represent the middle of each window
                key = ((wavelength//window)+0.5)*window
                if key in dict.keys() :
                    dict[key].append(intensity)
                else :
                    dict[key] = [intensity]
        fd.close()
    return dict

def is_corrupted(path,fichier):
    result= False
    presence = file_here(path)
    if presence[0]== False :
        print("No file named \"{}\" found".format(presence[1]))
        result = True        
    else :
        with open(fichier,'r') as fd:
            lines=fd.readlines()
            if len(lines)==0:    #If the file is empty
                print("The file is empty")
                result= True
            else:
                length_col1=0
                length_col2=0
                for line in lines:
                    values=line.strip().split()
                    if len(values)>=2:
                        if len(values)!=2 and (is_number(values[0]) and is_number(values[1])):
                            print("Data must be stored in two distinct columns on a same line")
                            result=True
                            break    
                        if len(values)==2 and (not(is_number(values[0])) and is_number(values[1])) or (is_number(values[0]) and not(is_number(values[1]))): #If only one of the two value is not a number
                            result=True
                            break
                        if is_number(values[0]) and is_number(values[1]):  #We check that the two values are number
                            length_col1+=1               #We count all values from both columns
                            length_col2+=1               
                    else:
                        if len(values)==1:
                            if is_number(values[0]):    #we add even if there is only one value
                                length_col1+=1
                    if length_col1!=length_col2:     #If both columns have different length the file is corrupt
                            result=True                    
    return result
