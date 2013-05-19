#!/bin/sh
# formatdir - outputs a directory listing in a friendly  and useful format.
gmk()
{
    #given input in kb,mb,or gb for best output format.
    if [ $1 -ge 1000000 ];then
	echo "$(scriptbc -p 2 $1 / 1000000)Gb"
    elif [ $1 -ge 1000 ];then
	echo "$(scriptbc -p 2 $1 / 1000)Mb"
    else
	echo "${1}kb"
    fi
}
if [ $# -gt 1 ];then
    echo "usage: $0 [dirname]" >&2;exit 1
elif [ $# -eq 1 ];then
    cd "$@"
fi
for file in *
do
    if [ -d "$file" ];then
	size=$(ls "$file" | wc -l | sed 's/[^[:digit:]]//g')
	if [ $size -eq 1 ];then
	    
