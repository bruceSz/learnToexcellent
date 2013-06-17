DEBUG=0

dirs="$(echo $PATH|sed 's/:/ /g')"

#for debug
[ $DEBUG == "1" ] && echo $dirs

for dir in $dirs
do
    #below i will ls the dir and check whether *java* exist.
    ls $dir|grep -i java  2>/dev/null >&2
    if [ $? = "0" ];then
    	echo "$dir contain java related program"
    fi

done