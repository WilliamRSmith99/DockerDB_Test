## Starting from official Postgres image
FROM postgres:latest

# ## Set DB creds 
ENV POSTGRES_PASSWORD="mysecretpassword"

## Add custom db configs to temp directory
ADD ./components/pg_hba.conf /tmp/pg_hba.conf

## Copy the prompt data into temp directory
COPY ./components/data.csv /tmp/data.csv

## New start script to start postgres, initialize the DB and run data import script
COPY  ./components/dbInit.sh /docker-entrypoint-initdb.d/dbInit.sh
COPY ./components/rockstarInit.sql /docker-entrypoint-initdb.d/rockstarInit.sql

## make above sh script executatble 
RUN chmod +x ./docker-entrypoint-initdb.d/dbInit.sh

## Expose port default postgres port (5432) on container
EXPOSE 5432 