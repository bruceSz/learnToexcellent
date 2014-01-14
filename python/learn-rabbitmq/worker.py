from common import init_channel
import time

def callback(ch,method,properties,body):
    print "[x] Received %r" %(body,)
    time.sleep(body.count('.'))
    print '[x] done'
    ch.basic_ack(delivery_tag=method.delivery_tag)

channel = init_channel('localhost')
channel.queue_declare(queue='hello',durable=True)

print "[*] Waiting for message. To exit press CTRL+C"

channel.basic_consume(callback,
                    queue="task_queue")

channel.start_consuming()

