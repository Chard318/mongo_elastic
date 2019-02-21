# use python3 as a parent image
FROM python:3

# set the working directory
WORKDIR /app

# copy the current directory contents including the profiles and the python script to upload the profiles into app folder
COPY . /app

# install packages from requirements
RUN pip install --no-cache-dir -r requirements.txt