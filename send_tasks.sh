#!/bin/sh
send_task () {
    dots=$(printf '.%.0s' $(eval "echo {1.."$(($1))"}"))
    docker run --rm --name rabbitmq_send_task rabbitmq-send-task ./new_task.py "Message #$1 $dots"
}

docker build -t rabbitmq-send-task -f send.Dockerfile .

for i in {1..10}
do
    send_task $i
done
