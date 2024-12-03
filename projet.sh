echo "Arguments :" $@
echo "Voulez vous graph sur toute l'échantillon ?(y/n)"
read r1
echo "Voulez vous sauvegarder les données à la fin de l'exécution ? (y/n)"
read s1
if [ $r1 == "y" ]
then 
    python3 'intensite.py' $@ | python3 'recherche_plot.py' 'a' 'a' $s1
else
    echo "Veuiller indiquer la longueur d'onde minimale de la fenetre"
    read t1
    echo "Veuiller indiquer la longueur d'onde maximale de la fenetre"
    read t2
    python3 'intensite.py' $@ | python3 'recherche_plot.py' $t1 $t2 $s1
fi