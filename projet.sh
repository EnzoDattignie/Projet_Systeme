echo "Arguments :" $@
flag=True #This flag stays at true while we want to execute the while loop and it is set to false when the user want to stop
loop=n #This flag allows to know if we are in the first loop or not
while [ $flag == True ]
do
    echo "Do you want to graph the entire sample ?(y/n)" #We ask the user for all necessary information
    read graphanswer
    limit1='null'
    limit2='null'
    if [ $graphanswer == "n" ]
    then #If the user does not want to graph the full sample, we ask for the upper and lower limits
        echo "Please enter the lower limit to graph"
        read limit1
        echo "Please enter the upper limit to graph"
        read limit2
    fi
    echo "Do you want to save the data after execution ?(y/n)"
    read saveanswer
    if [ $loop == "n" ] #If it's the first execution we pipe intensite.py in recherche_plot.py
    then
        python3 'intensite.py' $@ | python3 'recherche_plot.py' $limit1 $limit2 $saveanswer $loop
    else #if nth loop we only execute recherche_plot that will read a temporary file
        python3 'recherche_plot.py' $limit1 $limit2 $saveanswer $loop
    fi
    echo "Do you want to proceed ?(y/n)" #If the user desire to proceed y is affected to loop indicating a repetition, otherwise flag is set to false to finish execution
    read loop
    if [ $loop != "y" ]
    then
        flag=False
    fi
done
if [ -f "temp.txt" ];  #Checks if a temporary file exists in the directory
then 
    rm ./temp.txt #Removes the file created by recherche_plot.py
fi