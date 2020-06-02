#!/bin/bash

DIR=$1
contains_humans_dir='/home/ubuntu/videos/demo_contains_humans'
human_less_dir='/home/ubuntu/videos/demo_human_less'
simulate_dir='/home/ubuntu/cs293b-project/monitor/'$DIR
i=0

while [ $i -le 10 ]
   do
       BINARY=2
       T=1
       number=$RANDOM
       let "number %= $BINARY"
    
       if [ "$number" -eq $T ]
       then
           video_path=$(find $contains_humans_dir -type f | shuf -n 1)
       else
           video_path=$(find $human_less_dir -type f | shuf -n 1)
       fi
       if [ ! -f $simulate_dir`basename $video_path` ]
       then
	         ((i=i+1))
	         echo $video_path
	         cp $video_path $simulate_dir
	         sleep 5
       fi
done 