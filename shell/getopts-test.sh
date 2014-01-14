#!/bin/bash
echo "OPTIND starts at $OPTIND"

while getopts "pq:" optname
do
    case "$optname" in
	"p")
	    echo "option $optname is specified"
	    echo " and the OPTARG is $OPTARG"
        echo "this is p"
	    ;;
	"q")
	    echo "option $optname has value $OPTARG"
        echo "this is q"
	    ;;
	"?")
	    echo "unknown option $OPTARG"
        echo "this is ?"
	    ;;
	":")
	    echo "no argument value for option $OPTARG"
        echo "this is :"
	    ;;
	*)
	    echo "should not come to here"
        echo "this is nothing"
	    ;;
    esac
    echo "OPTIND is now $OPTIND"
done
