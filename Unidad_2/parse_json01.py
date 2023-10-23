'''
    Nombre: Jose Ricardo Hernandez Vazquez 
    Descripcion: Invocando REST API MapQuest
    Fecha: 23 de Octubre del 2023
'''

import urllib.parse
import requests

main_api = "https://www.mapquestapi.com/directions/v2/route?"
orig = "Washington"
dest = "Baltimore"
key = "Hq3SX0HDyLyF2B70fuex3hCN8LRMwyjo"
url = main_api + urllib.parse.urlencode({"key": key, "from":orig, "to":dest})
json_data = requests.get(url).json()
#Extraer distancia y timepo 
print(json_data['route']['sessionId'])
print(json_data['route']['distance'])
print(json_data['route']['time'])
#Extraer el primer elemento Legs el campo formattedTime 
formatted_time = json_data['route']['legs'][0]['_formattedTinme']
print(formatted_time)
