#This will prepare a elasticsearch node with mongo-connector enabled

FROM python:3

WORKDIR /app

COPY . /app 

# Installing Mongo Connector which will connect MongoDB and Elasticsearch
RUN pip install mongo-connector==2.1

RUN chmod +x startup.sh
#VOLUME /data

CMD ["./startup.sh"]
