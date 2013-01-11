#!/bin/bash
#filename:args.sh
echo "$#"
print(){
	echo "there are $# args"
	for arg in $*
	do
		echo $arg
	done
}
print $*
