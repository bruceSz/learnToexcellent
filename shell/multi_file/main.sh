#!/bin/bash
source common.sh
echo $main_env
cur=`pwd`
./m1.sh
./m2.sh
