#!/bin/bash
# q4_p2.sh

counter=1

while [ $counter -le 10 ]
do
	var=$(($counter%2))
	if [ $var -eq 0 ]; then
		file="even$counter"
		touch $file
		chmod 764 $file
	else
		file="odd$counter"
		touch $file
		chmod 554 $file
	fi
	((counter++))
done
