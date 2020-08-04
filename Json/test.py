import json
import pprint
with open('employees.json','r') as file:
    data = json.load(file)

printer = pprint.PrettyPrinter()


language = data.get('programming_language')
Emplyes = data.get('employees')
printer.pprint(language)

for employe in Emplyes:
    print(employe.get('id'),employe.get('fullname'))
    