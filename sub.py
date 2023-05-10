import pika

# establish a connection to RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# create a queue for the messages
channel.queue_declare(queue='message_queue')

# function to handle received messages
def callback(ch, method, properties, body):
    print("Received message: %r" % body)

# set up a consumer for the queue, using the callback function
channel.basic_consume(queue='message_queue',
                      on_message_callback=callback,
                      auto_ack=True)

# start consuming messages
print('Waiting for messages. To exit, press CTRL+C')
channel.start_consuming()

# close the connection
connection.close()