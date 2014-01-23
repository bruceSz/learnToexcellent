#!/bin/sh
function echon
{
	echo "$*"|awk '{printf "%s" $0}'
}
function echon2
{
	print "%s" "$*"
}
function echon3
{
	echo "$*"|tr -d '\n'
}
