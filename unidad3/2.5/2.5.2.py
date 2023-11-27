''' 
    Jose Ricardo Hernandez Vazquez 
    Descripcion: Ejercicio laboratorio 2.5 
    Fecha 27 nov 2023
'''
import json
import requests
requests.packages.urllib3.disable_warnings()

#Create a variable named api_url and assign the URL that targets the Loopback99 interface.

api_url = "https://192.168.56.101/restconf/data/ietf-interfaces:interfaces/interface=Loopback99"\
    
#Create a dictionary variable named headers that has keys for Accept and Content-type and assign the keys the value application/yang-data+json.


headers = {
            "Accept": "application/yang-data+json", 
            "Content-type":"application/yang-data+json"
          }
#Create a Python tuple variable named basicauth that has two keys needed for authentication, username and password.

basicauth = ("cisco", "cisco123!")

#Create a Python dictionary variable yangConfig holding the YANG data to create new interface Loopback99 
# (you use here the dictionary data from the Postman lab before, be aware that the JSON’s boolean true is in Python True wit
# h capital “T”):

yangConfig = {
        "ietf-interfaces:interface": {
            "name": "Loopback99",
            "description": "WHATEVER99",
            "type": "iana-if-type:softwareLoopback",
            "enabled": True,
            "ietf-ip:ipv4": { "address": [
                {
                    "ip": "99.99.99.99",
                    "netmask": "255.255.255.0"
                }
            ]
        },
        "ietf-ip:ipv6": {}
    }
}

