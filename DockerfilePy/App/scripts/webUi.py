import appUtils 

## Query Directory database for all addresses
table_results = appUtils.run_query("directorydb", "Directory", 'SELECT * FROM {}')

## Create  the html table body for each entry
table_body = ""
for entry in table_results:
    table_body += appUtils.GenerateHtmlTable(entry[0],entry[1],entry[2],entry[3],entry[4],entry[5],entry[6],entry[7])
    
print("Publishing HTML file")

## Open HTML template and inject table_body contents
with open("/app/html_resources/template.html", 'r') as file:
    lines = file.readlines()
 
## searches each line for comment, and inserts the table entry at line n+1        
for i, line in enumerate(lines):
    if "<!-- Table To be inserted below here -->" in line:
        
        lines.insert(i + 1, f"{table_body}\n")
        break
with open("/app/index.html", 'w') as file:
    file.writelines(lines)