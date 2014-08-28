from amqplib import client_0_8 as amqp

class PyAmqpLibPublisher(object):
    def __init__(self,exchange_name):
        self.exchange_name = exchange_name
        self.queue_exists = False

    def publish(self,message,routing_key):
        conn = amqp.Connection(host='127.0.0.1',userid = 'guest',password='guest',virtual_host = '',insist = False)
        ch = conn.channel()
        ch.exchange_declare(exchange=self.exchange_name,type = 'fanout',durable=False,auto_delete=False)
        msg = amqp.Message(message)
        msg.properties['content_type'] = 'text/plain'
        msg.properties['delivery_mode'] = 2
        ch.basic_publish(exchange=self.exchange_name,
                            routing_key=routing_key,
                            msg = msg)

        ch.close()
        conn.close()
