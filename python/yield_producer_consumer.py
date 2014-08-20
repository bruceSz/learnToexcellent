import random

def get_data():
    return random.sample(range(10),3)

def consume():
    running_sum = 0
    data_items_seen = 0

    while True:
        datas = yield
        data_items_seen += len(datas)
        running_sum += sum(datas)
        print 'running sum is {}'.format(running_sum)
        print 'items seen so far is {}'.format(data_items_seen)
        print('the running average is {}'.format(running_sum/data_items_seen))

def produce(consumer):
    while True:
        datas = get_data()
        print('producing {}'.format(datas))
        consumer.send(datas)
        yield

if __name__ == '__main__':
    consumer = consume()
    consumer.send(None)
    p = produce(consumer)
    for _ in range(10):
        next(p)

