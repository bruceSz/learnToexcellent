# edited by song zhang 2012-03-08
# below are commit limits :
#
# 	Mail address below [author] are limits
# 	which can limit the git log ouput to those 
# 	commit records only related to corresponding
# 	mail address. To add more address ,follow the 
# 	format of commented line "mailaddx:ab@cd.com"
# 	where x represent a number bigger than that of
# 	previous line.
# 	
# 	time span below [time-limit] are limits
# 	which can limit git log ouput to those
# 	commit records only satisfy those time between 
# 	these time span. You can add more time limit 
# 	as you wish.
#
[remoteinfo]

targetdir:/home/szhang/tornado

targetmachine:127.0.0.1

targetuser:szhang

targetuserpasswd:2009101523
#[savedfile]


[author]

mailadd1:berrange@redhat.com
mailadd2:laine@laine.org
mailadd3:mkletzan@redhat.com
#mailaddx:xx@xx.com



[time-limit]

time-span1:2012-01-01==2012-03-08
#time-spanx:xx==xx 
