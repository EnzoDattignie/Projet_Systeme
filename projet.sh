echo "Arguments :" $@
echo "Veuiller indiquer la longueur d'onde minimale de la fenetre"
read t1
echo "Veuiller indiquer la longueur d'onde maximale de la fenetre"
read t2
python3 'intensite.py' $@ | python3 'recherche_plot.py' $t1 $t2