import psycopg2
from psycopg2 import sql
import requests
import json
import urllib.parse

def run_query(database_name, table_name, query):
    db_connection_params = {
        'dbname': f"{database_name}",
        'user': 'rockstaruser',
        'password': 'Gt@6',
        'host': '172.22.48.1',
        'port': '35432',
    }
    try:
        print(f"Executing SQL Query...\nDatabase: {database_name}\nTable: {table_name}\nQuery: {query}")
        connection = psycopg2.connect(**db_connection_params)
        ## Create a cursor object to execute SQL queries
        cursor = connection.cursor()

        ## Use the sql module to safely format table names and column names
        query = sql.SQL(f"{query}").format(sql.Identifier(table_name))

        ## Execute the query
        cursor.execute(query)

        ## Try to get results, if query that produces results
        ## Catch returns rows affected by query using INSERT, UPDATE, or DELETE 

        results = cursor.fetchall()
        connection.commit()
        
        return results
        
        

    except psycopg2.Error as e:
        print(f"Error: {e}")
    finally:
        ## Close the cursor and connection
        if cursor:
            cursor.close()
        if connection:
            connection.close()
            
def validateAddr(street, city, state):
    params = {
    'auth-id': '158b949a-2ec2-79e8-d9d0-b7c1cf00c9e6',
    'auth-token': '2Hb17YXu1Ei6ZVXriKRm',
    'license': 'us-core-cloud',
    'street': street,
    'city': city,
    'state': state,
    'candidates': 10,
    }
    response = requests.get('https://us-street.api.smarty.com/street-address', params=params)
    if (len(response.json()) > 0):
        return True
    else:
        return False
            
def urlEncodeString(string):   
    encoded_string = urllib.parse.quote(string)
    return encoded_string

def GenerateHtmlTable(First,Last,Address,City,State,ZipCode,Country,valid):
    tableTemplate = f"<tr class='{valid}'><td>{First}</td><td>{Last}</td><td>{Address}</td><td>{City}</td><td>{State}</td><td>{ZipCode}</td><td>{Country}</td><td>{valid}</td></tr>"
    return tableTemplate

