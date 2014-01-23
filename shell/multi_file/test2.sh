echo this is bash
echo $$
ps -ef|grep $$|grep -v grep |grep -v ps
