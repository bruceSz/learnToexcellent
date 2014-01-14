import sys
from common import init_channel
message = " ".join(sys.argv[1:]) or "hello world"
channel = init_channel('localhost')
channel.queue_declare(queue="task_queue",durable=True)

message = " ".join(sys.argv[1:]) or "hello world"

channel.basic_publish(exchange='',
                    routing_key="task_queue",
                    body = message,
                    properties=pika.BasicProperties(
                        delivery_mode=2,
                        ))

print "[x] Send %r" %(message,)
channel.close()
