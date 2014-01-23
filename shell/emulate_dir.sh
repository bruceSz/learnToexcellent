#!/bin/sh
# DIR pretends we 're the DIR 

function usage
{
    cat < EOF >&2
    Usage: $0 [DOS flags] directory or directories
    where:
	/D	 sort by columns
	/H	show help for this shell script
	/N	show long listing format with filenames on right
    EOF
    exit 1
}

postcmd=""
flags=""
while [ $# -gt 0 ]
do
    case $1 in
	/D	) flags="$flags -x" ;;
	/H	) usage;;
	/[NOW]	) flags="$flags -l";;
    esac
    shift
done

echo $@
if [ ! -z "postcmd" ] ;then
    ls $flags "$@" |$postcmd
else
    ls $flags "$@"
fi
