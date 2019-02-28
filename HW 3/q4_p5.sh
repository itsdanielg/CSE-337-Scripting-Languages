#!/bin/bash
# q4_p5.sh

if [ $# -eq 0 ]; then
    echo "No arguments entered."
    exit 1
fi

touch temp.txt

for num in "$@"
do
    if ! [[ "$num" =~ ^[0-9]+$ ]]; then
        echo "Invalid parameters. Only numbers are accepted."
        rm temp.txt
        exit 1
    fi
    echo $num >> temp.txt
done

min=$(sort -n temp.txt | head -1)
max=$(sort -n temp.txt | tail -1)

var=$(($#%2))
((median=$#/2))
if [ $var -eq 0 ]; then
    bottom=$(sort -n temp.txt | head -$((median)) | tail -1)
    top=$(sort -n temp.txt | head -$((median+1)) | tail -1)
    median=$(bc <<< "scale = 2; (($top + $bottom) / 2)")
else
    median=$(sort -n temp.txt | head -$((median+1)) | tail -1)
fi

echo "The min is $min"
echo "The max is $max"
echo "The median is $median"

rm temp.txt