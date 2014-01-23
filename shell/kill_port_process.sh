#!/bin/bash
name=$(lsof -i:80|tail -1|awk '"$1"!=""{print $2}')
if [ -z $name ];then
    echo "no process can be used to killed"
    exit 0
fi

id=$(lsof -i:80|tail -l|awk '"$1"!=""{print $2}')
kill -9 $id
echo "process name=$name($id) killed!"
exit 0
