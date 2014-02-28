#!/bin/bash
# the || and && has same preference.

f() {
    sleep $1
    echo $1
}

while [ -n "$1" ];
do
    f $1 &
    shift
done
wait
