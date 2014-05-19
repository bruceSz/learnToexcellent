import pika
import sys

parameters = pika.ConnectionParameters(host = 'localhost')
connection = pika.BlockingConnection(parameters)
channel = connection.channel()
channel.queue_declare(queue='task_queue',durable=True)
message = ' '.join(sys.argv[1:]) or 'hello world'

channel.basic_publish(exchange='',
                        routing_key='task_queue',
                        body=message,
                        properties=pika.BasicProperties(
                                delivery_mode = 2,
                                ))

print '[x] Send %r'%(message,)
connection.close()
