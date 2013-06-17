#!/bin/sh
# unrm - search the deleted files archive for the specified file or directory.
# if there is more than matching result,shows a list of the results.
# ordered by timestamp,and lets the user specify which one to restore.

mydir="$HOME/.deleted-files"
realrm="/bin/rm"
move="/bin/mv"
dest=$(pwd)

if [ ! -d $mydir ];then
    echo "$0:no deleted files directory: nothing to unrm" >&2;exit 1
fi
cd $mydir
if [ $# -eq 0 ];then
    echo "contents of your deleted files archive(sorted by date)"
    ls -FC |sed -e 's/\([[:digit:]][[:digit:]]\.\)\{5\}//g' \
	-e 's/^/ /'
    exit 0
fi
matches="$(ls *"$1" 2> /dev/null |wc -l)"
if [ $matches -eq 0 ];then
    echo "no match for \"$1\" in the deleted file archive.">&2
    exit 1
fi
if [ $matches -gt 1 ];then
    echo "more than one file or directory match in the archive"
    index=1
    for name in $(ls -td *"$1")
    do
	datetime="$(echo $name|cut -c1-14| \
awk -F. 'print $5"/"$4" at "$3":"$2":"$1 }' )"
	if [ -d $name ];then
	    size="$(ls $name|wc -l|sed 's/[^[:digit:]]//g')"
	    echo " $index) $1 (size=${size}kb,deleted=$datetime)"
	else
	    size="$(ls -sdk1 $name|awk '{print $1}')"
	    echo " $index) $1 (size = ${size}kb,deleted = $datetime)"
	fi
	index=$(($index + 1))
    done
    echo ""
    echo  -n "which version of $1 do you want to restore('0' to quit)?[1]:"
    read desired
    if [ ${desired:=1} -ge $index ];then
	echo "$0:restore canceled by user:index value too big" >&2
	exit 1
    fi
    if [ $desired -lt 1 ];then
	echo "$0:restore canceled by user" >&2;exit 1
    fi
    restore="$(ls -td1 *"$1"|sed -n "${desired}p")"
    if [ -e "$dest/$1" ];then
	echo "\"$1\" already exists in this directory .cannot overwrite.">&2
	exit 1
    fi
    echo -n "restoring file"
    $move "$restore" "$dest/$1"
    echo "done."
    echo -n "delete the additional copies of this file[y]"
    read answer
    if [ ${answer:=y} = 'y' ];then
	$realrm -rf *"$1"
	echo "deleted"
    else
	echo "additional copies retained"
    fi
else
    if [ -e "$dest/$1" ];then
	echo "\"$1\" already exists in this directory.cannot overwrite ." >&2
	exit 1
    fi
    restore="$(ls -d *"$1")"
    echo -n "restoring file \"$1\""
    $move "$restore" "$dest/$1"
    echo "done"
fi
exit 0



