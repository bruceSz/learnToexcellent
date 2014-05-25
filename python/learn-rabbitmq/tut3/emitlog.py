import pika
import sys
connection = pika.BlockingConnection(pika.ConnectionParameters(
                                            host='localhost'))

channel = connection.channel()

channel.exchange_declare(exchange='logs',
                            type='fanout')

message = ' '.join(sys.argv[1:]) or 'hello world'
channel.basic_publish(exchange='logs',
                        routing_key = '',
                        body = message)

print "[x] Send %r"%(message,)
connection.close()


