FROM python:3.11-alpine

WORKDIR /usr/src/app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY new_task.py .

ENV RABBITMQ_HOST="172.17.0.1"
CMD [ "python", "-u", "./new_task.py" ]
