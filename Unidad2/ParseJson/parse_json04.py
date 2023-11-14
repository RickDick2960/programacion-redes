'''
    Nombre: Jose Ricardo Hernandez Vazquez 
    Descripcion: Invocando REST API MapQuest
    Fecha: 23 de Octubre del 2023
'''

import urllib.parse
import requests

while True:
    orig = input("Starting Location: ")
    if orig == "quit" or orig == "q":
        #Mensaje de despedida
        print("Mensaje de despedida")
        break
    
    dest = input("Destination: ")
        #Mensaje de despedida
    if dest == "quit" or dest == "q":
        print("Mensaje de despedida")
    break
    
    
    
    

    main_api = "https://www.mapquestapi.com/directions/v2/route?"

    key = "Hq3SX0HDyLyF2B70fuex3hCN8LRMwyjo"

    url = main_api + urllib.parse.urlencode({"key": key, "from":orig, "to":dest})
    json_data = requests.get(url).json()

    print("URL: " + (url))  

    json_data = requests.get(url).json()
    json_status = json_data["info"]["statuscode"]

  