import json
import sys
import char

import eventlet
from eventlet.green import urllib2

urls = ["http://caifu.baidu.com/wealth/ajax?pageSize=10&pageNum=72&module=Finance&category=wealth&serverTime=1395236211044&pvid=1395236211041855&resourceid=1800181&subqid=1395236211041855&sid=ui%3A0%26bsInsurance%3A2%26bsInvest%3A2&pssid=0&tn=NONE&signTime=41&qid=0&wd=&zt=self&amount=0&cycle=0&expectedProfitRate=0&profitType=0&risk=0&productType=3101%2C3103%2C3104%2C3102"]

def fetch(url):
        req = urllib2.Request(url)
        return urllib2.urlopen(req).read()

pool = eventlet.GreenPool()
for body in pool.imap(fetch,urls):
	print "got body",len(body)

        print body.decode('UTF-8').encode(sys.getfilesystemencoding())

