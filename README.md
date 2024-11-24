# Projet_Systeme

Ce programme a été réalisé dans le cadre de l'UE HAI727I de la faculté des sciences de Montpellier.

Pour executer ce programme, exécuter dans la cmd "./projet.sh filepath fenetre" par exemple  "./projet.sh Spectre_photoluminescence.txt 7"

Notre programme a pour but de lire un fichier de sortie d'un spectrometre avec comme valeur la longueur d'onde et l'intensité séparés par un espace et un saut de ligne entre chaque entrée. 

Les bibliothèques à importer sont sys,os,re,matplotlib.
La taille de la fenetre initiale est de 10 nm.

Ce programme est composé de 4 fichiers. 
Un script bash projet.sh demandant a l'utilisateur le chemin, la fenetre et les valeurs sur lesquelles faire un graphique
Un script fonction.py contenant des fonctions necessitant un appel de la part des autres programmes.
Un script intensité.py lisant les informations dans le fichier texte fourni et les organisant dans un dictionnaire dont les clefs sont les longueur d'onde au centre des fenetres.
Un script recherche_plot.py lisant les informations transmises par intensite.py et réalisant une liste a l'aide des clefs et des moyennes d'intensité et affichant sur les longueurs d'ondes demandées  

Nos Choix:
Premierement nous avons fait le choix de réaliser le script fonctions dont l'unique but est de stocker nos fonctions usuelle tels que le minimum ou le maximum qui peut etre utilisé par plusieurs scripts.
Nous avons également choisi d'utiliser le stdin pour pipe un script a l'autre pour éviter la création d'un fichier texte temporaire ou la lecture indépendante du meme fichier deux fois. 
Ce choix nous a limité dans la maniere de prendre en compte le input la fonction input de python essayant de lire le standard input nous avons donc a la place demandé les arguments depuis le script bash et donné en argument au programme.
Nous avons décidé de normaliser le graphique pour que sa valeur max vaille 1 ainsi nous pouvons plus aisément comparer différents résultats enttre eux sachant que l'unité d'intensité lue par un spectrometre est rarement indiquée ni importantes
