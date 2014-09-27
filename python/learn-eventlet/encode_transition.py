# -*- coding:utf-8 -*-

def transition(ori,encoding):
    ret = unicode(ori,encoding)
    return ret
    

astr='\u4e2d\u56fd\u5e73\u5b89'

print transition(astr,'utf-8')
print transition(astr,'ascii')
print transition(astr,'ISO-8859-1')
print transition(astr,'gb2312')
print transition(astr,'utf-16')
