#!/bin/sh
# nicenumber -- given a number ,shows it in comma-separated form.
# expects dd and td to be instantiated.Instantiates  nicenum
# or,if a second arg is specified,the output is echoed to stdout.
nicenumber()
{
    # note that we assume that '.' is the decimal separator in
    # the input value to this script.the decimal separator in
    # the output value is '.' unless specified by the user with -d flag
    integer=$(echo $1|cut -d. -f1)
    decimal=$(echo $1|cut -d. -f2)
    if [ $decimal != $1 ];then
	#there's a fractional part,so let's include it.
	result = "${DD:="."}$decimal"

}
