#!/bin/sh
# validint -- validates integer input,allowing negative ints too.

function validint
{
    # validate first field .Then test against min value $2 and/or
    # max value $3 if they are supplied.If they are not supplied,skip these tests.
    number="$1"; min="$2"; max="$3"
    if [ -z $number ];then
	echo "you didn't enter anything.Unacceptable." >&2; return 1
    fi
    if [ "${number%${number#?}}" = "-" ];then
	testvalue="${number#?}"
    else
	testvalue="$number"
    fi
    nodigits="$(echo $testvalue|sed 's/[[:digit:]]//g')"
    if [ ! -z $nodigits ];then
	echo "Invalid number format! Only digits,no commas,spaces,etc." >&2
	return 1
    fi
    if [ ! -z $min ];then
	if [ "$number" -lt "$min" ];then
	    echo "you value is too small:smallest value is $min" >&2
	    return 1
	fi
    fi	
    if [ ! -z $max ];then
	if [ "$number" -gt "$max" ];then
	    echo "your value is too big:largest acceptable value is $max" >&2
	    return 1
	fi
    fi
    return 0
}
if validint "$1" "$2" "$3"; then
    echo "that input is a valid integer value within your constraints"
fi
