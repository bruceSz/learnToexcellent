#!/bin/sh
# validAlphaNum - Ensure that input consists only of alphabetical
# and numeric characters.
validAlphaNum()
{
    # return 0 if all upper+lower+digits,1 otherwise
    # remove all unacceptable chars
    compressed="$(echo $1|sed -e 's/[^[:alnum:]]//g')"
    if  [ "$compressed" != "$input" ];then
	return 1
    else
	return 0
    fi
}
# sample usage of this function in a script
echo -n  "enter input":

read input
if ! validAlphaNum "$input" ;then
    echo "you input mush consist of only letters and numbers." >&2 
    exit 1
else
    echo "input is valid"
fi
exit 0
