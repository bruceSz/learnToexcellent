#!/bin/bash
#filename: password.h
echo -e "enter password:"
stty -echo
read password
stty echo 
echo 
echo $password
echo Password read
