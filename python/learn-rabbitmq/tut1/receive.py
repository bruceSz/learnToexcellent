#import pika
#
#def callback(ch,method,properties,body):
#    print "[x] Received %r" %(body,)
#
#connection = pika.BlockingConnection(pika.ConnectionParameters(
#    'localhost'
#    ))
#channel = connection.channel()
#channel.queue_declare(queue="hello")
#channel.basic_consume(callback,
#                    queue = "hello",
#                    no_ack = True)
#
#
#
#print '[*] Waiting for message.To exit press CTRL+C'
#channel.start_consuming()
import pika
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare('hello')
print '[*] Waiting for message.To exit press CTRL+C'

def callback(ch,method,properties,body):
    print body

channel.basic_consume(callback,queue='hello',no_ack=True)
channel.start_consuming()

