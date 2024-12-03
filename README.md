# Projet_Systeme
This programm was realised for the Module HAI727I in Faculté des Sciences of Montpellier

To install this program you only need to clone the git in the repository of your choice and verify that your installation of pythons have the following libraries installed : sys, os, re, matplotlib.

To execute for the first time you first need to open the cmd in your repository and type "chmod 555 ./projet.sh" then for any execution you only need to type "./project.sh filepath window" with filepath being the path to the file you want to analyse and window being the precision you want to exploit your data in nanometers, it is initially set to 10, for exemple "./project.sh Spectre_photoluminescence.txt 7".

Our program was made to read an outpuut file of a specrometer with wavelength and intensity separated by a space and data separated by a line break between each input. 

This program is composed of 4 main files. A bash script "projet.sh" gathering from the user the filepath, the window and the minimum and maximum wavelength to graph on. And 3 python scripts, function.py containing useful functions for other scripts, intensite.py reading the data from the file and storing each intensity to it's own wavelength window named by the center of the window and then passing it through the stdin to the script recherche_plot.py printing result and graphing it in the given range of intensity.   

Choices :
First we made the choice to realise the additionnal script function to have a cleaner project and store the common functions like minimum or maximum used by both scripts. We also chose the stdin to pipe a script to another to avoid the creation of an external txt file. This choice limited us in the way to take the input into acount as we could not ask the user in the python script anymore so we used project.sh to take all the inputs. We also decided to normalise the graph so iit's maximum value is equal to one, this way we can easily compare multiple graphs even from different spectrometers knowing that a spectrometer's intensity read is rarely in SI unit and depends huighly in experimental conditions.  