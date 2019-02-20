FROM ubuntu

COPY . /

RUN apt-get update && \
	apt-get install -y curl

RUN chmod +x index.sh
RUN chmod +x test.sh

CMD ["./index.sh"]
