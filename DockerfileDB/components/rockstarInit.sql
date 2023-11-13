-- Create a new app database
CREATE DATABASE directorydb;

-- Connect to the new database
\c directorydb;

-- Create a new table named 'Directory'
CREATE TABLE "Directory" (
    "First Name" varchar (150),
    "Last Name" varchar (150),
    "Address" varchar (150),
    "City" varchar (150),
    "State" varchar (150),
    "Zip Code" varchar (150),
    "Country" varchar (150),
    "valid" varchar (150)
);
-- Import the prompt data from csv -> 'Directory' table
COPY "Directory" FROM '/tmp/data.csv' WITH CSV HEADER;

-- Create Rockstar Service User with privledges only to app Db and table
CREATE USER rockstaruser;
GRANT ALL PRIVILEGES ON DATABASE directorydb TO rockstaruser;
GRANT ALL PRIVILEGES ON TABLE public."Directory" TO rockstaruser;
ALTER USER postgres with PASSWORD 'Gt@6';
ALTER USER rockstaruser with PASSWORD 'Gt@6';