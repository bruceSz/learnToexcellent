#!/usr/bin/bash

wait_time=10
total=0
sleep_time=2

while true;do
    if [  -e ~/test.lock ];then
        echo "test server started ~"
        break
    fi
    total=$((total+$sleep_time))
    sleep $sleep_time

    if [ $total -ge $wait_time  ];then
        echo "test server has not started in $wait_time sec."
        exit 1
    fi
done
