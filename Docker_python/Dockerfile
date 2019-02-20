# use python as a parent image
FROM python:3

# set the workind directory
WORKDIR /app

# copy the current directory contents into app folder
COPY . /app

# install packages from requirements
RUN pip install --no-cache-dir -r requirements.txt