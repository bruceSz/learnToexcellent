#!/bin/bash
Usage() {
    echo "Usage: set_k_v.sh -k xx -v yy -f Filename.
    This script will update xx=*(* here is arbitrary literal value)
    with xx=yy ,if xx not exist,create key-value pair:xx=yy."
}

if [ A"$*" = A ];then
    Usage
    exit 3
fi

key=""
value=""
filename=""

while getopts "k:v:f:" optname 
do
	case "$optname" in
		"k")
            key=$OPTARG
            ;;
        "v")
            value=$OPTARG
            ;;
        "f")
            filename=$OPTARG
            ;;
        "?")
            echo "Unknow option $OPTARG"
            Usage
            exit 4
            ;;
        ":")
            echo "No argument provided for option $OPTARG"
            Usage
            exit 5
            ;;
        "*")
            echo "should not come here!!!"
            exit 6
	esac
done

if [ A"$key" = A -o A"$value" = A -o A"$filename" = A ];then
    Usage
    exit 7
fi

echo "$key"
echo "$value"
echo "$filename"

#sed -i 's/${key}/${key}=${value}/' $filename
sed -i "s/${key}.*/${key}=${value}/"  $filename
