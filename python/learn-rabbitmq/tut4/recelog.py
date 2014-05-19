
import pika
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters(
                                host='localhost'))
channel = connection.channel()
channel.exchange_declare(exchange='direct_logs',
                            type='direct')

result = channel.queue_declare(exclusive=True)
queue_name = result.method.queue
severity = sys.argv[1]

channel.queue_bind(exchange='direct_logs',
                    queue=queue_name,
                    routing_key=severity)

print '[*] Waiting for logs.To exit press CTRL+c'

def callback(ch,method,properties,body):
    print '[x] %r'%(body,)

channel.basic_consume(callback,
                        queue=queue_name,
                        no_ack=True)

channel.start_consuming()
