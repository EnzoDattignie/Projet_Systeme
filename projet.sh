echo "Arguments :" $@
flag=True #Ce flag vérifie que l'on veut répeter la boucle while, elle est set a false lorsque l'utilisateeur veut arreter
boucle=n #Ce flag permet de savoir si on est dans une répétition de la boucle originale pour ne pas réexécuter du code inutile
while [ $flag == True ]
do
    echo "Voulez vous graph sur toute l'échantillon ?(y/n)" #On demande a l'utilisateur toutes les informations nécessaires
    read r1
    t1='null'
    t2='null'
    if [ $r1 == "n" ]
    then #Si on ne veut pas graph sur tout l'échantillon on demande les bornes min et max
        echo "Veuiller indiquer la longueur d'onde minimale de la fenetre"
        read t1
        echo "Veuiller indiquer la longueur d'onde maximale de la fenetre"
        read t2
    fi
    echo "Voulez vous sauvegarder les données à la fin de l'exécution ?(y/n)"
    read s1
    if [ $boucle == "n" ] #Si premiere exécution on pipe intensite.py dans recherche_plot.py
    then
        python3 'intensite.py' $@ | python3 'recherche_plot.py' $t1 $t2 $s1 $boucle
    else #si n-ieme exécution on exécute uniquement recherche_plot qui lira un fichier temporaire
        python3 'recherche_plot.py' $t1 $t2 $s1 $boucle
    fi
    echo "Voulez vous continuer ?(y/n)" #Si l'utilisateur veut continuer boucle passe a y ce qui indique qu'on entre dans une répétition mais le flag reste a true, sinon le  flag passe a false et on arrete
    read boucle
    if [ $boucle != "y" ]
    then
        flag=False
    fi
done
rm ./temp.txt #Supression du fichier temporaire créé par recherche_plot.py
