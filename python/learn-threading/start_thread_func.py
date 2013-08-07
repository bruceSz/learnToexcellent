import threading

def thread_func(num):
	for n in range(0,int(num)):
		print "i come from %s,num: %s" %(threading.currentThread().getName(),n)


def main(thread_num):
	thread_list = list()
	for i in range(0,thread_num):
		thread_name = "thread_%s"%i
		thread_list.append(threading.Thread(target=thread_func,name=thread_name,args=(20,)))
	for thread in thread_list:
		thread.start()
	for thread in thread_list:
		thread.join()

if __name__ == '__main__':
	main(3)
