## Starting from official Postgres image
FROM ubuntu:20.04

## build arg so NGINX install noninteractive
ARG DEBIAN_FRONTEND=noninteractive

## Update base image
RUN apt update && apt upgrade -y 

## Add Python 3.10 & pip
RUN apt install python3 -y
RUN apt install python3-pip -y

## Install python dependencies
RUN pip install psycopg2-binary requests 

## Add Nginx
RUN apt install nginx -y

## create app home dir
RUN mkdir app
COPY ./App ./app/

## add custom nginx config file to nginx directory
COPY  ./nginx.conf /etc/nginx/nginx.conf

## Add container startup script and make it executable 
COPY ./docker-entrypoint.sh ./docker-entrypoint.sh
RUN chmod +x ./docker-entrypoint.sh

## Expose port 8080 on container, per instructions
EXPOSE 8080 

ENTRYPOINT [ "/bin/bash" ]
CMD [ "./docker-entrypoint.sh" ]