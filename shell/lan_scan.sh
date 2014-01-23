net_info=`ifconfig|egrep '\<inet\>'|grep -v 127|grep -v 192`
net_addr=`echo $net_info|awk '{print $2}'`
net_broadcast=`echo $net_info|awk '{print $3}'`
net_mask=`echo $net_info|awk '{print $4}'`

echo addr is `echo $net_addr|awk -F : '{print $2}'`
echo broadcast is `echo $net_broadcast|awk -F: '{print $2}'`
echo mask is `echo $net_mask|awk -F: '{print $2}'`

nums=`seq 254`
for num in $nums;do
    echo 9.181.88.$num
    ping -q -c 1 9.181.88.$num|grep statics|grep -v grep
done


