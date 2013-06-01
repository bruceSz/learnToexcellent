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
	result="${DD:="."}$decimal"
    fi
    thousands=$integer
    while [ $thousands -gt 999 ];do
	remainder=$(($thousands % 1000))
	while [ ${#remainder} -lt 3 ];do
	    remainder="0$remainder"
	done
	thousands=$(($thousands / 1000))
	result="${TD:=","}${remainder}${result}"
    done
    nicenum="${thousands}${result}"
    if [ ! -z $2 ];then
	echo "$nicenum"
    fi
}
DD="."
TD=","
while getopts "d:t:" opt;do
    case $opt in
	d ) DD="$OPTARG"  ;;
	t ) TD="$OPTARG"  ;;
    esac
done
shift $(($OPTIND - 1))
if [ $# -eq 0 ];then
echo "Usage: $(basename $0) [-d c] [-t c] numberic value"
echo "  -d specified the decimal point delimiter (default '.')"
echo "  -t specified the thousands delimiter (default ',')"
exit 0
fi
nicenumber $1 1 
exit 0
