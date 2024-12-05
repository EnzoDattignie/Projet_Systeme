echo "Arguments :" $@
flag=True
boucle=n
while [ $flag == True ]
do
    echo "Voulez vous graph sur toute l'échantillon ?(y/n)"
    read r1
    echo "Voulez vous sauvegarder les données à la fin de l'exécution ?(y/n)"
    read s1
    t1='null'
    t2='null'
    if [ $r1 == "n" ]
    then
        echo "Veuiller indiquer la longueur d'onde minimale de la fenetre"
        read t1
        echo "Veuiller indiquer la longueur d'onde maximale de la fenetre"
        read t2
    fi
    if [ $boucle == "n" ]
    then
        python3 'intensite.py' $@ | python3 'recherche_plot.py' $t1 $t2 $s1 $boucle
    else
        python3 'recherche_plot.py' $t1 $t2 $s1 $boucle
    fi
    echo "Voulez vous continuer ?(y/n)"
    read boucle
    if [ $boucle != "y" ]
    then
        flag=False
    fi
done
