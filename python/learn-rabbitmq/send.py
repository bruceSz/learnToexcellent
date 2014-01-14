
from common import init_channel

channel = init_channel('localhost')

channel.queue_declare(queue="hello")
channel.basic_publish(exchange='',
                    routing_key="hello",
                   body="hello world")
print "[x] Send 'hello world'"
