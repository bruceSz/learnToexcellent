
#from common import init_channel
#
#channel = init_channel('localhost')
#
#channel.queue_declare(queue="hello")
#channel.basic_publish(exchange='',
#                    routing_key="hello",
#                   body="hello world")
#print "[x] Send 'hello world'"
import sys
import pika
def declare_hello_send(message):
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    channel.queue_declare(queue='hello')

    channel.basic_publish(exchange='',routing_key='hello',body=message)
    print '[x] sent: '+message+"'\n"
    channel.close()

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print "message is empty!"
        sys.exit(0)
    message = sys.argv[1]
    declare_hello_send(message)
    


