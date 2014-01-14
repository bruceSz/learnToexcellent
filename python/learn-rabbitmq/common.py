import pika
def init_channel(node_address):
    
    connection = pika.BlockingConnection(pika.ConnectionParameters(
        node_address
        ))
    channel = connection.channel()
    return channel
