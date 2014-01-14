import pika
import sys
from common import init_channel
channel = init_channel('localhost')

channel.exchange_declare(exchange="logs",
                        type="fanout")
message = " ".join(sys.argv[1:]) or "info: hello world!"
channel.basic_publish(exchange='logs',
                    routing_key='',
                    body=message)
print "[x] Send %r" %(message,)
#connection.close()


