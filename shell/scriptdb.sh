#!/bin/sh
# scriptbc - wrapper for 'bc' that returns the result of a caculation.
if [ $1 = "-p" ];then
    precision=$2
    shift 2
else
    precision=2
fi
bc -q <<EOF
scale=$precision
$*
EOF
exit 0
