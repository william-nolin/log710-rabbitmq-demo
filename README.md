# Démo de RabbitMQ pour le cours Log710
Ce dépôt contient une démo simulant un système distribué contenant une instance de RabbitMQ, 4 noeuds de calculs et un noeud envoyant des messages.
Le but de ce projet est de démontrer l'utilisation de RabbitMQ afin de distribuer des tâches à un ou plusieurs noeuds de calculs.
Afin d'utiliser cette démo, vous devez avoir installé sur votre ordinateur:
 - Docker
 - Docker-compose
 - Un shell (sh, bash, zsh, ...)

Le dépôt contient trois scripts afin de démarrer rapidement la simulation:
 - start.sh: Démarrage de RabbitMQ et des noeuds de calcul dans Docker
 - send_tasks.sh: Envoie de 10 tâches à RabbitMQ
 - stop.sh: Éteint les conteneurs Docker démarrés précédement

Afin de simuler une charge de travail, les messages envoyés aux noeuds de calcul contiennent un ou plusieurs points, qui détermine la longueur du travail. 
Par exemple, le message "......" correspond à un travail de 6 secondes.
Les messages sont communiqués dans la queue nommée ```tasks```.

Les noeuds de calcul et les noeud envoyant les messages sont des scripts Python 3.11 situés dans les fichier ```worker.py``` et ```new_task.py```.
Leur contenu est basé sur la deuxième partie du tutoriel de RabbitMQ, ["Work Queues"](https://www.rabbitmq.com/tutorials/tutorial-two-python.html).

## Architecture du système
![image](https://github.com/william-nolin/log710-rabbitmq-demo/assets/113483515/218a3f9c-2a13-46a8-905c-2d5007818ffc)

## Fonctionnalités démontrées dans cette démo
 - Queues de message
 - Équilibrage de la charge entre chaque noeud de calcul
 - Persistance des messages (afin de survivre à un crash de RabbitMQ)
 - ```ack``` des messages après la fin du travail
 - Authentification basique
 - API Python de RabbitMQ (Pika)

## Accéder à l'interface de gestion de RabbitMQ
L'interface de gestion de RabbitMQ est disponible à l'adresse ```localhost:15672```.

## Changer le nombre de noeuds de calculs
La démo est pré-configurée avec 4 noeuds de calculs qui reçevront les messages depuis RabbitMQ.
Afin de changer le nombre d'instances, il suffit de changer la ligne 21 du fichier ```docker-compose.yaml```.
