import zmq
import random
import time

context = zmq.Context()

sender = context.socket(zmq.PUSH)
sender.bind("tcp://*:5557")

print "press enter when workers are ready"
_ = raw_input()
print "sending tasks to workers"

sender.send("0")

random.seed()

total_msec = 0
for task_nbr in range(100):
    workload = random.randint(1,100)
    total_msec += workload
    sender.send(str(workload))

print "total expected cost:%s msec"%total_msec
