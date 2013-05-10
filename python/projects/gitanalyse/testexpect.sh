#usr/bin/bash

host="127.0.0.1"
username="szhang"
password="2009101523"
src_file="tmp"
dest_file="x"

expect expectscp.sh $host $username $password $src_file $dest_file>/dev/null
