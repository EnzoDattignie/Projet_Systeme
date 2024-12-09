# Projet_Systeme
This program was developped for the HAI727I module at the Faculty of Science, University of Montpellier.

To install this program, simply clone the Git repository into the directory of your choice and ensure that your Python installation includes the following libraries : sys, os, re, matplotlib, datetime.

When running this program for the first time, open the command prompt in the appropriate directory and execute the following command:  
chmod 555 ./projet.sh     
For subsequent executions, use the command:     
./project.sh filepath window  
Here, filepath represents the path to the file you wish to analyse and window specifies the precision (in nanometer) for data analysis. By default, the precision is set to 10 nm.
#### Exemple command:  
./project.sh Spectre_photoluminescence.txt 7  

Our program is designed to process output files from spectrometers, where each line contains a wavelength and its corresponding intensity, separated by a space.

## Program Structure  
This program consists of 4 main files: 
1. projet.sh : A Bash script that collects inputs from user including the filepath, the window size and the wavelength range to plot. 
2. function.py : A Python scrpit containing useful functions (e.g., for finding minimum and maximum values) used by other scripts.
3. intensite.py : Reads the data from the input file, assigns each intensity value to a corresponding wavelength window (centered on the sepecified precision).
4. recherche_plot.py : Processes the data receives through stdin, generates the results, and plot the graph within the specified wavelength range.

## Design Choice
- We created an additionnal script, fonction.py, to keep the project organized by storing each fonctions in a separate file.
- Instead of generating an external text file, we opted to use the stdin to pipe data between scrpits. This decision simplifies danta handling but required centralising user inputs in the Bash script (projet.sh).
- We normalized the graph so that its maximum value is equal to one, ensuring consistent visual representation. This approach allows us to easily compare multiple graphs, even from different spectrometers, as intensity is rarely measured in SI units and typically depends on experimental conditions.
