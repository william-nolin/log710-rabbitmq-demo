#!/usr/bin/env python
import pika

message='Hello World!'
queue_name='hello'

# On se connecte à l'instance RabbitMQ à l'adresse "localhost:5672"
credentials = pika.PlainCredentials('admin', 'asecurepassword')
parameters = pika.ConnectionParameters('localhost',
                                       5672,
                                       '/',
                                       credentials)
connection = pika.BlockingConnection(parameters)
channel = connection.channel()

# Crée une queue de message nommée "hello"
channel.queue_declare(queue=queue_name)

# Envoie le message à RabbitMQ
channel.basic_publish(exchange='',
                      routing_key=queue_name,
                      body=message)
print(f" [x] Message envoyé: {message}")

connection.close()
