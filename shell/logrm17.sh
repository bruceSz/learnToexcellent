#!/bin/sh
# logrm - logs all file deletion requests unless the -s flag is used.
removelog="/var/log/remove.log"
if [ $# -eq 0 ];then
    echo "usage: $0 [-s ] list of file or directories"  >&2
    exit 1
fi
if [ "$1" = "-s" ];then
    shift
else
  echo "$(date):${USER}: $@">> $removelog
fi
/bin/rm "$@"
exit 0

