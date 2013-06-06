#!/bin/sh

# newrm,a replacement for the existing rm command,provides a
# rudimentary unremove capability by creating and utilizing a new
# directory within the user's home directory.It can handle directories
# of content as well as individual files,and if the user specifies
# -f flag files are removed and not archived.

mydir="$HOME/.deleted-files"
realrm="/bin/rm"
copy="/bin/cp -R"

if [ $# -eq 0 ];then
    exec $realrm # our shell is replaced by /bin/rm
fi
flag=""
while getopts "dfiPRrvW" opt
do
    case $opt in
	f) exec $realrm "$@"    ;;
	*) flags="$flags -$opt" ;;
    esac
done
if [ ! -d $mydir ];then
    if [ ! -w $HOME ];then
	echo "$0 failed: can't create $mydir in $HOME" >&2
	exit 1
    fi
    mkdir $mydir
    chmod 700 $mydir
fi
for arg
do
    newname="$mydir/$(date "+%S.%M.%H.%d.%m").$(basename "$arg")"
    if [ -f "$arg" ];then
	$copy "$arg" "$newname"
    elif [ -d "$arg" ];then
	$copy "$arg" "$newname"
    fi
done

exec $realrm $flag "$@"



