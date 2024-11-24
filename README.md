# Projet_Systeme
Pour executer ce programme, exécuter dans la cmd "./projet.sh filepath fenetre" par exemple  "./projet.sh Spectre_photoluminescence.txt 7"

Ce programme a été réalisé dans le cadre de l'UE HAI727I de la faculté des sciences de Montpellier.

Notre programme a pour but de lire un fichier de sortie d'un spectrometre avec comme valeur la longueur d'onde et l'intensité séparés par un espace et un saut de ligne entre chaque entrée. 

Les bibliothèques à importer sont sys,os,re,matplotlib.
La taille de la fenetre initiale est de 10 nm.

Ce programme est composé de 4 fichiers. 
Un script bash projet.sh demandant a l'utilisateur le chemin, la fenetre et les valeurs sur lesquelles faire un graphique
Un script fonction.py contenant des fonctions necessitant un appel de la part des autres programmes.
Un script intensité.py lisant les informations dans le fichier texte fourni et les organisant dans un dictionnaire dont les clefs sont les longueurs d'onde au centre des fenetres.
Un script Spectre_photoluminescence.py lisant les informations transmises par intensite.py et réalisant une liste a l'aide des clefs et des moyennes d'intensité et affichant sur les longueurs d'ondes demandées.
