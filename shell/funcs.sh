#!/bin/bash
import (){
    # currently you can only use the 'import filename' syntax
    if [ $1 ];then
        commands=`cat $1`
        
    else
        echo "import must be provided with sh-file name."
        exit 1
    fi
}

str=`cat test.sh`
bash -c $str

