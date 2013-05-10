#!/bin/bash
#newrm,a replacement for the existing  rm command,provides a
# rudimentary unremove capability by creating and utilizing a new
# directory within the user's name directory.it can handle directories
# of content as well as individual files.And if the user specifies
# the -f flag files are removed and not mode to trash-box.
mydir="$HOME/.deleted-files"
realrm="/bin/rm"
copy="/bin/cp -R"
if [ $# -eq 0 ];then
    exec $realrm  # our shell is replaced by /bin/rm
fi
# parse all options looking for '-f'
flags=""
while getopts "dfiPRrvW" opt
do
    case $opt in
	f) exec $realrm "$@" ;;# exec lets us exit this script directly.
	*) flags="$flags -$opt" ;;
    esac
done
shift $(($OPTIND - 1))
#make sure that the $mydir exists
if [ ! -d $mydir ];then
    if [ ! -w $HOME ];then
	echo "$0 failed:can't create $mydir in $HOME" >&2
	exit 1
    fi
    mkdir $mydir
    chmod 700 $mydir
fi
for arg
do
    newname="$mydir/$(date "+%s.%M.%H.%d.%m").$(basename "$arg")"
    if [ -f "$arg" ];then
	$copy "$arg" "$newname"
    elif [ -d "$arg" ];then
	$copy "$arg" "$newname"
    fi
done
exec $realrm $flags "$@"



