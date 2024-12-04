# Projet_Systeme
This programm was realised for the Module HAI727I at the Faculty of Science of Montpellier University.

To install this program you only need to clone the git in the repository of your choice and check if your installation of pythons have the following libraries installed : sys, os, re, matplotlib, datetime.

The first time you execute the programm you need to open the cmd in the right repository and type "chmod 555 ./projet.sh" then for any execution you only need to type "./project.sh filepath window" with filepath being the path to the file you want to analyse and window being the precision you want to exploit your data in nanometers, it is initially set to 10 nm. 
Here is an exemple of a typical command : "./project.sh Spectre_photoluminescence.txt 7".

Our program was made to read an output file of a spectrometer with each wavelength and intensity separated by a space while each data being on a new line.

This program is composed of 4 main files. A bash script 'projet.sh' gathering from the user the filepath, the window as well as the minimum and maximum wavelength to graph on. 
Three python scripts, 'function.py' containing useful functions for other scripts, 'intensite.py' reading the data from the file and storing each intensity to its own wavelength window named by its corresponding center, then passing it through the standard input (stdin) to the script 'recherche_plot.py' which prints the result and graphs it in the given range of wavelength.   

Choices :
First we made the choice to realise the additionnal script function to have a cleaner project and store the common functions like minimum or maximum used by both scripts. We also chose the stdin to pipe a script to another to avoid the creation of an external txt file. This choice limited us because the input was not taken into account as the user wasn't asked to provide bounds in the python script anymore. Therefore, we used 'project.sh' to centralized the inputs. We also decided to normalize the graph so its maximum value is equal to one. This way we can easily compare multiple graphs even from different spectrometers knowing that intensity is rarely measured in SI units whith intensity units usually depending on experimental conditions.
