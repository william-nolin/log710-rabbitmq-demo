#!/usr/bin/env python
import pika, sys, os, time

rabbitmq_host=os.environ['RABBITMQ_HOST']
queue_name='tasks'

def callback(ch, method, properties, body):
    print(f" [x] Reçu: {body.decode()}")

    # On simule un long calcul en attendant une seconde par point dans le message reçu
    time.sleep(body.count(b'.'))

    # On informe RabbitMQ que le calcul est terminé, le message peut être supprimé
    ch.basic_ack(delivery_tag=method.delivery_tag)

    print(" [x] Fini")

def main():
    # On se connecte à l'instance RabbitMQ
    credentials = pika.PlainCredentials('admin', 'asecurepassword')
    parameters = pika.ConnectionParameters(rabbitmq_host,
                                           5672,
                                           '/',
                                           credentials)
    connection = pika.BlockingConnection(parameters)
    channel = connection.channel()
    
    # On s'assure que la queue de message existe
    channel.queue_declare(queue=queue_name, durable=True)

    # Demande à RabbitMQ de ne pas envoyé plus d'un message à la fois
    # Tant que le message n'aura pas été ack, le worker n'en reçevera pas de nouveau
    channel.basic_qos(prefetch_count=1)
    
    # On se souscrit à la queue en définissant la fonction "callback" comme consomateur
    channel.basic_consume(queue=queue_name,
                          on_message_callback=callback)

    # On attend de reçevoir des messages
    print(' [*] En attente de messages. Pour sortir, appuyer sur CTRL+C')
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
