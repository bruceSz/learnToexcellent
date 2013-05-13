#!/bin/sh
#locate - searchs the locate database for specified pattern
locatedb="/var/locate.db"
exec grep -i "$@" $locatedb
