#coding=utf-8
def UCaseChar(ch):
    if ord(ch) in range(97,122):
        return chr(ord(ch)-32)
    return ch
def LCaseChar(ch):
    if ord(ch) in range(65,91):
        return chr(ord(ch)+32)
    return ch

def UCase(str):
    return ''.join(map(UCaseChar,str))
def LCase(str):
    return ''.join(map(LCaseChar,str))
print(LCase('ABC,abc'))
print(UCase('abc,ABC'))
    
