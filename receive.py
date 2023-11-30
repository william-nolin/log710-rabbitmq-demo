#!/usr/bin/env python
import pika, sys, os

queue_name='hello'

def callback(ch, method, properties, body):
    print(f" [x] Received {body}")

def main():
    # On se connect à l'instance RabbitMQ à l'adresse "localhost:5672"
    credentials = pika.PlainCredentials('admin', 'asecurepassword')
    parameters = pika.ConnectionParameters('localhost',
                                           5672,
                                           '/',
                                           credentials)
    connection = pika.BlockingConnection(parameters)
    channel = connection.channel()
    
    # On s'assure que la queue de message existe
    channel.queue_declare(queue=queue_name)
    
    # On se souscrit à la queue en définissant la fonction "callback" comme consomateur
    channel.basic_consume(queue=queue_name,
                          auto_ack=True,
                          on_message_callback=callback)

    # On attend de reçevoir des messages
    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
