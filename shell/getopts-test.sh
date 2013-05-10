#!/bin/bash
echo "OPTIND starts at $OPTIND"
while getopts "pq:" optname
do
    case "$optname" in
	"p")
	    echo "option $optname is specified"
	    echo " and the OPTARG is $OPTARG"
	    ;;
	"q")
	    echo "option $optname has value $OPTARG"
	    ;;
	"?")
	    echo "unknown option $OPTARG"
	    ;;
	":")
	    echo "no argument value for option $OPTARG"
	    ;;
	*)
	    echo "should not come to here"
	    ;;
    esac
    echo "OPTIND is now $OPTIND"
done
