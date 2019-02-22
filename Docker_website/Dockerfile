FROM python:3.7
RUN pip3 install --upgrade pip
COPY ./shellfish /opt/shellfish
RUN pip3 install -r /opt/shellfish/requirements.txt
ENV DOCKER_CONTAINER=1
EXPOSE 8080 
WORKDIR /opt/shellfish
RUN chmod +x manage.py
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8080"]
