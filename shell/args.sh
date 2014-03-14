#!/bin/bash
#filename:args.sh
echo $0
echo "$#"
echo "the arg in position 0 is: " $0
print(){
	echo "there are $# args"
	for arg in $*
	do
		echo $arg
	done
}
print $*
