#!/bin/bash
DIR=$1
if [[ $DIR == */ ]]
then
    DIR=${DIR::-1}
fi
echo $DIR
inotifywait -m $DIR -e create -e moved_to |
    while read dir action file; do
        if [[ $file == *.mkv ]]
	then
	    python3 -W ignore detect_human_monitor.py --path $DIR/$file
        fi	
    done
