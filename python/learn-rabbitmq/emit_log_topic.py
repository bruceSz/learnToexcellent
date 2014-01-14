from common import init_channel
import sys

channel = init_channel('localhost')

channel.exchange_declare(exchange='topic_logs',
                        type='topic')
routing_key = sys.argv[1] if len(sys.argv) > 1 else 'anonymous.info'

message = ' '.join(sys.argv[2:]) or 'hello world'
channel.basic_publish(exchange='topic_logs',
                        routing_key=routing_key,
                        body=message)

print '[x] Send %r:%r' %(routing_key,message)

