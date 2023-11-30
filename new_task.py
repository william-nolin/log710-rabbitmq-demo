#!/usr/bin/env python
import pika, sys, os

rabbitmq_host=os.environ['RABBITMQ_HOST']
message=' '.join(sys.argv[1:]) or 'Hello World!'
queue_name='tasks'

# On se connecte à l'instance RabbitMQ à l'adresse "localhost:5672"
credentials = pika.PlainCredentials('admin', 'asecurepassword')
parameters = pika.ConnectionParameters(rabbitmq_host,
                                       5672,
                                       '/',
                                       credentials)
connection = pika.BlockingConnection(parameters)
channel = connection.channel()

# Crée une queue de message
channel.queue_declare(queue=queue_name, durable=True)

# Envoie le message à RabbitMQ
channel.basic_publish(exchange='',
                      routing_key=queue_name,
                      body=message,
                      properties=pika.BasicProperties(
                          delivery_mode = pika.spec.PERSISTENT_DELIVERY_MODE    # On s'assure que le message va survivre un crash de RabbitMQ
                      ))
print(f" [x] Message envoyé: {message}")

connection.close()
