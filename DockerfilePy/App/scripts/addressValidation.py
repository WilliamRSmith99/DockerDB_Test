import appUtils 
import time

## Since this script is the first to execute, I am adding a 10 second wait to ensure that the postgres container is ready to recieve connections 
time.sleep(10)

## Initial test with known address to demonstrate accurate functionality of address validation API.
print(f"Validating the following address:\nStreet: 45 Main st,\nCity: Yonkers,\nState: NY,\nZip Code: 10701,")
response = appUtils.validateAddr('45 Main st','Yonkers','NY')
print("Valid: " + str(response))
print("##########################################################")

## Query Directory database for all addresses
table_results = appUtils.run_query("directorydb", "Directory", 'SELECT "Address", "City", "State", "Zip Code", "Country" FROM {}')

## Loop through each address checking validity and commiting the answer to the Directory Database
for address in table_results:
    print(f"Validating the following address:\nStreet: {address[0]},\nCity: {address[1]},\nState: {address[2]},\nZip Code: {address[3]},")
    response = appUtils.validateAddr(address[0], address[1], address[2])
    response = False
    print("Valid: " + str(response))
    appUtils.run_query("directorydb", "Directory", f"UPDATE \"Directory\" SET \"valid\" = '{response}' WHERE \"Address\" = '{address[0]}' RETURNING *;")
    print("##########################################################")