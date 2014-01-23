#!/bin/sh
# inpath - verifies that a specified program is either valid as is,
# or that it can be found in the PATH directory list.
in_path()
{
    #given a command and the PATH,try to find the command.Returns
    # 0 if found and executable, 1 if not.Note that this is temporarily
    # modifies the IFS,but restores it upon completion.
    cmd=$1 path=$2 retval=1
    oldIFS=$IFS IFS=":"
    for directory in $path
    do
	if [ -x $directory/$cmd ];then
	    retval=0
	fi
    done
    IFS=$oldIFS
    return $retval
}
checkForCmdInPath()
{
    var=$1
    # The variable slicing notation in the following conditional
    # needs some explanation:${var#expr} returns everything after
    # the mach for 'expr' in the variable value (if any) ,and
    # ${var%expr} returns everything that does not match(in this
    # case) ,just the very first character.You can also do this in Base
    # with ${var:0:1},and you could use cut too:cut -c1
    if [ "$var" != "" ];then
	if [ "$var%${var#?}" = "/" ];then
	    if [ ! -x $var ];then
		return 1
	    fi
	elif ! in_path $var $PATH;then
	    return 2
	fi
    fi
}
if [ $# -ne 1 ];then
    echo "Usage: $0 command " >&2;exit 1
fi
checkForCmdInPath "$1"
case $? in
    0) echo "$1 found in PATH"   ;;
    1) echo "$1 not found or note executable"  ;;
    2) echo "$1 not found in PATH"
esac
exit 0


