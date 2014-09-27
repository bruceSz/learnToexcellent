import urllib2
import sys
import chardet

req = urllib2.Request('http://caifu.baidu.com/wealth/ajax')
content = urllib2.urlopen(req).read()

typeEncode = sys.getfilesystemencoding()
infoencode = chardet.detect(content).get('encoding','utf-8')
print "system encode :",typeEncode
print 'content encode:',infoencode


print unicode(content)

