import pika
from common import init_channel
channel = init_channel('localhost')
channel.exchange_declare(exchange='logs',
                        type='fanout')
result = channel.queue_declare(exclusive=True)
queue_name = result.method.queue

channel.queue_bind(exchange='logs',
                    queue=queue_name)

print '[x]  Waiting for logs. To exit press CTRL+C'

def callback(ch,method,properties,body):
    print '[x] %r' %(body,)

channel.basic_consume(callback,
                        queue=queue_name,
                        no_ack=True)
channel.start_consuming()

