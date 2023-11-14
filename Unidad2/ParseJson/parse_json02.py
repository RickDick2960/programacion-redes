'''
    Nombre: Jose Ricardo Hernandez Vazquez 
    Descripcion: Invocando REST API MapQuest
    Fecha: 23 de Octubre del 2023
'''

import urllib.parse
import requests

main_api = "https://www.mapquestapi.com/directions/v2/route?"
orig = "San Ocote"
dest = "San Miguel de allende "
key = "Hq3SX0HDyLyF2B70fuex3hCN8LRMwyjo"
url = main_api + urllib.parse.urlencode({"key": key, "from":orig, "to":dest})
json_data = requests.get(url).json()

print("URL: " + (url))

json_data = requests.get(url).json()
json_status = json_data["info"]["statuscode"]

if json_status == 0:
    print("API Status: " + str(json_status) + " = A successful route call.\n")
#Codificar para manejar el error distinto a Cero.
else:
    print("API Status: " + str(json_status) + " = Error.")