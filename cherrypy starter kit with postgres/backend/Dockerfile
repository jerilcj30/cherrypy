FROM python:3.10.7-slim-buster

# add requirements.txt to the image
ADD requirements.txt /app/requirements.txt

# create the necessary directories
WORKDIR /app

# install python dependencies
RUN pip install -r requirements.txt