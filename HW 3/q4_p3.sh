#!/bin/bash
# q4_p3.sh

echo "Please enter a sentence:"
read sentence
char="k"
echo "Number of occurrences of 'k':"
echo $sentence | grep -o "k" | wc -l