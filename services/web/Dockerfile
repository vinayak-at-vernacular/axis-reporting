FROM python:3.8.1-slim-buster


RUN apt-get update && apt-get install -y libaio1 curl unzip

RUN curl -L -O https://v8r-oracle-client.s3.ap-south-1.amazonaws.com/19.5/instantclient19.5.zip && \
    unzip instantclient19.5.zip -d /usr


ENV LD_LIBRARY_PATH /usr/lib:/usr/local/lib:/usr/instantclient_19_5
ENV PKG_CONFIG_PATH=/usr/instantclient_19_5

# set work directory
WORKDIR /opt/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt /opt/app/requirements.txt
RUN pip install -r requirements.txt

EXPOSE 5002

# copy project
COPY . /opt/app/

# CMD [ "python", "manage.py", "runserver", "0.0.0.0:5002" ]