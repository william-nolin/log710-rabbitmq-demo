#!/bin/sh

docker-compose up -d rabbitmq
sleep 5
docker-compose up worker
