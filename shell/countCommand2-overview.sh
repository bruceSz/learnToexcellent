#!/bin/sh
# how many commands:a simple script to count how many executable
# commands are in your current PATH

myPath="$(echo $PATH|sed -e 's/ /~~/g' -e 's/:/ /g')"
count=0;nonex=0
for dirname in $myPath;do
	directory="$(echo $dirname |sed 's/~~/ /g')"
	if [ -d  "$directory" ];then
		for command in $(ls "$directory");do
			if [ -x "$directory/$command" ];then
				count="$(($count + 1))"
			else
				nonex="$(($nonex + 1))"
			fi
		done
	fi
done
echo "$count commands,and $nonex entries that weren't executable"
exit 0
