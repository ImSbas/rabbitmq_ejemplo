import pika

# establish a connection to RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# create a queue for the messages
channel.queue_declare(queue='message_queue')

# loop to receive messages from the terminal and publish them to the queue
while True:
    message = input("Enter a message: ")
    channel.basic_publish(exchange='',
                          routing_key='message_queue',
                          body=message)
    print("Sent message: %r" % message)

# close the connection
connection.close()