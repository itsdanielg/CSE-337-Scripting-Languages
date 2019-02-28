#!/bin/bash
# q4_p1.sh

dirArg=$1

if [ $# -eq 1 ]
then
    if [ -d "${dirArg}" ]; then
        echo "Current shell is: $SHELL"
        cd $dirArg
        echo "Current directory is : $PWD"
        echo "Home directory is : $HOME"
        echo ""
        echo "— 5 most recently modified non-empty subdirectories—"
        ls -d */ -l -t | head -5
        echo ""
        echo "— Files in last 45 minutes"
        find . -type f -size -1000c -mmin -45
        echo ""
        echo "======================================================================"
    else
        echo "$dirArg is not a directory."
    fi
else
    echo "No arguments given."
fi
