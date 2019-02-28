#!/bin/bash
# q4_p4.sh

dirArg=$1

if [ $# -eq 1 ]
then
    if [ -d "${dirArg}" ]; then
        cd $dirArg
        total=$(find . -maxdepth 1 -type d -not -name ".*" | wc -l)
        echo "Number of directories under $dirArg: $total"
    else
        echo "$dirArg is not a directory."
    fi
else
    echo "No arguments given."
fi
