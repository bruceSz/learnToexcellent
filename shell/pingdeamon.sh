#!/bin/bash
#filename:pingdeamon.sh
while true
do
	ping 9.181.137.98 >out.tmp &
	ping_pid=$!
	sleep 3
	if [ ! -z out.tmp ];then
		echo "connected with 9.181.137.98"
		exit 0
	fi
	
	kill -9 ${ping_pid}
	echo "can not connect to 9.181.137.98 ,will try again."
	sleep 61
done
