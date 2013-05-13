#!/bin/sh
# mklocatedb - builds the locate database using find. must be root
# to run this script.

locatedb="/var/locate.db"
if [ "$(whoami)" != "root" ];then
    echo "must be root to run this command." >&2
    exit 1
fi

find / -print > $locatedb
exit 0
