import sys
from functions import *
import matplotlib.pyplot as plt
import datetime
import select

#Check that data is available on the stdin
flag = select.select([sys.stdin], [], [], 1)[0]  #We wait up to 1 second

#Initialization of lists to store data
wavelength = []
intensity = []

if flag:      #Data read from stdin
    stdin_data=list(sys.stdin)
    if len(stdin_data) == 0:
        print("The file is corrupted")
        sys.exit(1)
    if sys.argv[4] == "n" :
        for line in stdin_data : #We read the stdin line by line to get the data piped by intensite.py
            l = line.split()
            if len(l) >= 3 :
                print (line.strip()) #We show lines not printed because of the pipe and we store the wavelength and the average intensity in their respective list
                if l[0] == "Wavelength":
                    wavelength.append(float(l[2].strip('"')))
                if l[0] == 'Average':
                    intensity.append(float(l[2].strip()))
                    print('---------------------------------------') #Purely visual separation line, we got the idea from the project made by José Felix and Alban Dessouter
else:          #Reading data from temp.txt
    with open("temp.txt","r") as temp:
        for l in temp :
            line = l.split()
            wavelength.append(float(line[0]))
            intensity.append(float(line[1]))     


inf = sys.argv[1].strip() 
sup = sys.argv[2].strip()

if is_number(inf) and is_number(sup): #If those are numbers we change them into floats, otherwise we take the min and max from the list wavelength
    inf_ = float(inf)
    sup_ = float(sup)
    if sup_<inf_:          #sup and inf are permuted if sup<inf
        sup_,inf_=inf_,sup_
else:
    print('No values provided as limits. Plotting the entire sample')
    if (len(wavelength) > 0) : #Simply avoids an error if the sample is empty
        inf_ = wavelength[minimum(wavelength)]
        sup_ = wavelength[maximum(wavelength)]
    else :
        inf_ = 0
        sup_ = 0

#These lists will be the ones plotted between the two wavelength limits provided by the user
wavelengthf=[] 
intensityf=[]
for i in range(len(wavelength)):  #Creation of both lists
    if inf_ <= wavelength[i] <=sup_:        
        wavelengthf.append(wavelength[i])
        intensityf.append(intensity[i])

#We normalize the intensity
if len(intensity) > 0 :
    Imax=intensity[maximum(intensity)]
else :
    Imax = 0
intensityf_normalised=[]
for i in range(len(intensityf)):
    intensityf_normalised.append(intensityf[i]/Imax)
plt.plot(wavelengthf,intensityf_normalised,label='I(λ)',color='red')
plt.ylim(-0.10,1.10)
plt.legend()
plt.xlabel("Wavelength (λ)")
plt.ylabel("Intensity (I)")
plt.title("Graph showing intensity as a function of the wavelength")

with open("temp.txt","w") as temp :
    for i in range(0,len(intensity)) :
        temp.write("{}\t{}\n".format(wavelength[i],intensity[i]))

if len(wavelengthf)>0: #We check that lines aren't empty before ploting
    if sys.argv[3] == 'y': #If the user want to save we generate a text and a picture with a filename made from the timestamp
        filename = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
        with open(filename+"_save.txt",'w') as save :
            for i in range (0,len(intensityf_normalised)) :
                save.write("{}\t{}\n".format(wavelengthf[i],intensityf_normalised[i]))
        plt.savefig(filename)
    plt.show()
else:
    print('No data available for graphing in this interval')
