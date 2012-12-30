#!/bin/bash
#filename :ifs.sh
data="name,sex,rollno,location"
oldIFS=$IFS
IFS=","
for item in $data
 do
  echo item:$item
 done
IFS=$oldIFS
