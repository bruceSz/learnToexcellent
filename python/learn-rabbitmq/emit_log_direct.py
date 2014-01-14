import pika
import sys

from common import init_channel

channel = init_channel('localhost')
channel.exchange_declare(exchange='direct_logs',
                        type='direct')

serverity = sys.argv[1] if len(sys.argv) > 1 else 'info'
message = ' '.join(sys.argv[2:]) or "hello world!"
channel.basic_publish(exchange='direct_logs',
                    routing_key=serverity,
                    body=message)
print '[x] Send %r:%r' %(serverity,message)



