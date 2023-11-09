## Starting from official Postgres image
FROM postgres:latest

## Set DB creds 
ENV POSTGRES_PASSWORD="mysecretpassword"
ENV POSTGRES_USER="root"
ENV POSTGRES_DB="directoryDB"

## Copy the Prompt data into the contianer
COPY ./data.xlsx /tmp/data.xlsx

## New start script to start postgres and run data import script
COPY ./startup.sh /docker-entrypoint-initdb.d/startup.sh
RUN chmod +x /docker-entrypoint-initdb.d/startup.sh

EXPOSE 5432