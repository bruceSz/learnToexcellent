import pika
import sys


connection = pika.BlockingConnection(pika.ConnectionParameters(
                                            host='localhost'))

channel = connection.channel()

channel.exchange_declare(exchange='direct_logs',
                            type='direct')
severity = sys.argv[1] if len(sys.argv) > 1 else 'info'
print severity


message = ' '.join(sys.argv[2:]) or 'hello world'
print message

channel.basic_publish(exchange='direct_logs',
                        routing_key = severity,
                        body = message)

print "[x] Send %r"%(message,)
connection.close()
