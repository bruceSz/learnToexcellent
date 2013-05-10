#!/bin/sh
retries = "10"
action = "lock"
nullcmd ="/bin/true"
while getopts "lur:" opt;do
    case $opt in
	l) action = "lock" ;;
	u) action = "unlock";;
	r) retries = "$OPTARG";;
    esac
done
shift $(($OPTIND -1))
if [ $# -eq 0 ];then
    cat <<EOF >&2

Usage: $0 [-l|-u] [-r retries] lockfilename
where -l requests a lock (the default),-u requests an unlock,-r x
specifies a maximum number of retries before it fails (default = $retries)
EOF
exit 1
fi
if [ -z "$(which lockfile|grep -v '^no')" ];then
    echo "$0 failed: 'lockfile' utility not found in PATH" >&2
    exit 1
fi
if [ "$action" = "lock"]; then
    if ! lockfile -1 -r $retries "$1" 2> /dev/null; then
	echo "$0: failed: couldn't create lockfile in time" >&2
	exit 1
    fi
else
    if [ ! -f "$1" ];then
	echo "$0: warning : lockfile $1 doesn;t exist to unlock">&2
	exit 1
    fi
    rm -f "$1"
fi
exit 0
