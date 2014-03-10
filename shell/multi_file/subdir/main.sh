#!/bin/bash
main_env='this is main '
script_dir=`dirname $0`
echo $script_dir
source $script_dir/m1.sh
source $script_dir/m2.sh
