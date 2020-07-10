FROM python:3.8.1-slim-buster


RUN apt-get update && apt-get install -y libaio1 curl unzip

RUN curl -L -O https://v8r-oracle-client.s3.ap-south-1.amazonaws.com/19.5/instantclient19.5.zip && \
    unzip instantclient19.5.zip -d /usr

# RUN wget https://download.oracle.com/otn_software/linux/instantclient/19600/instantclient-basiclite-linux.x64-19.6.0.0.0dbru.zip && \
#     unzip instantclient-basiclite-linux.x64-19.6.0.0.0dbru.zip && \
#     rm -f instantclient-basiclite-linux.x64-19.6.0.0.0dbru.zip 



# WORKDIR /opt/oracle/instantclient-basiclite-linux.x64-19.6.0.0.0dbru


# RUN rm -f *jdbc* *occi* *mysql* *jar uidrvci genezi adrci && \
#     # echo /opt/oracle/instantclient* > /etc/ld.so.conf.d/oracle-instantclient.conf && \
#     # ldconfig
#     ln -s libclntshcore.so.12.1 libclntshcore.so && \
#     ln -s libclntsh.so.12.1 libclntsh.so && \
#     ln -s libocci.so.12.1 libocci.so && \
#     ln -s libsqora.so.12.1 libsqora.so

# COPY . /opt/app/oracle

ENV LD_LIBRARY_PATH /usr/lib:/usr/local/lib:/usr/instantclient_19_5
ENV PKG_CONFIG_PATH=/usr/instantclient_19_5

# ENV LD_LIBRARY_PATH /opt/oracle/instantclient-basiclite-linux.x64-19.6.0.0.0dbru
# ENV ORACLE_BASE /opt/oracle/instantclient-basiclite-linux.x64-19.6.0.0.0dbru
# ENV ORACLE_HOME /opt/oracle/instantclient-basiclite-linux.x64-19.6.0.0.0dbru

# RUN mkdir lib

# COPY /opt/oracle/instantclient-basiclite-linux.x64-19.6.0.0.0dbru/libclntsh.so /lib/
# COPY /opt/oracle/instantclient-basiclite-linux.x64-19.6.0.0.0dbru/libclntshcore.so /lib/  
# COPY /opt/oracle/instantclient-basiclite-linux.x64-19.6.0.0.0dbru/libocci.so /lib/
# COPY /opt/oracle/instantclient-basiclite-linux.x64-19.6.0.0.0dbru/libsqora.so /lib/

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