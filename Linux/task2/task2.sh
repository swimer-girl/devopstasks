#!/bin/bash
source ./task2.config

#Create the locking dir if it doesn't exist
if [[ ! -d "/lockdir/" ]]; then 
    mkdir -p /lockdir/
fi
for file in $SOURCEDIR/*
do
#Check if there is currently a lock in place, if so then exit, if not then create a lock
	if [ -f $file.lock ]; then 
		echo "task2 is currently already running"
		exit
	else
		touch $file.lock
		firststr=$(head -n 1 $file)
		laststr=$(tail -n 1 $file)
	
		UUID="^[0-9a-fA-F]{8}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{12}"
		if [[ $laststr =~ $UUID ]]
		then
			fname=$(head -n 1 $file | awk '{print $1}')
			fdate=$(head -n 1 $file | awk '{print $2}')
			lastfmod=$(date -d "@$( stat -c '%Y' $file )" +'%Y%m%d_%H%M%S')
			newfname="${fname}_${fdate}_${lastfmod}"
			mv $file $TARGETDIR/$newfname
			timelog=$(date +"%Y-%m-%d %H:%M:%S")
			echo "$timelog file $file moved to $TARGETDIR/$newfname" >> $LOGFILENAME
			rm $file.lock
			continue
		else 
		rm $file.lock
		fi
	fi
done
