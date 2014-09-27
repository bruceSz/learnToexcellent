import multiprocessing
import os

def get(url,lock):
    lock.acquire()
    print os.getpid(),url
    lock.release()

plist = []
lock = multiprocessing.Lock()
for i in ['www.sina.com.cn','www.163.com','www.baidu.com','www.cnblogs.com','www.qq.com']:
    proc = multiprocessing.Process(target=get,args=(i,lock))
    plist.append(proc)

for proc in plist: 
    proc.start()

for proc in plist:
    proc.join()

