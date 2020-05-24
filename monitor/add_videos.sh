#!/bin/bash

contains_humans_dir='/home/ubuntu/videos/contains_humans_mega'
human_less_dir='/home/ubuntu/videos/human_less_mega'

simulate_dir='/home/ubuntu/cs293b-project/monitor/test_temp'

# generate a boolean true/false
BINARY=2
T=1
number=$RANDOM
let "number %= $BINARY"

if [ "$number" -eq $T ]
#if [$RANDOM%2 -eq 0]
then
    video_path=$(find $contains_humans_dir -type f | shuf -n 1)
    #echo containsHuman
    echo $video_path
else
    video_path=$(find $human_less_dir -type f | shuf -n 1)
    #echo noHuman
    echo $video_path
fi

cp $video_path $simulate_dir

