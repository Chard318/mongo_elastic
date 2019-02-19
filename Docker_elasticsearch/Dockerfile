FROM ubuntu

COPY . /

RUN apt-get update && \
	apt-get install -y curl

RUN chmod +x index.sh

CMD ["/index.sh"]