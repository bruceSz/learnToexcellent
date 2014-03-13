
echo $0
parse_para $*
echo "$SCHEMA"
parse_para $*

echo "$SCHEMA"
if [ "$SCHEMA" != "Distributed" ];then
    echo not all in one 
fi
