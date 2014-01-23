#!/bin/bash
i=0
while true
do
	echo $i 
        if [ $i -eq  9 ];then
		exit 0
	fi
	i=$(($i+1))
done
	

