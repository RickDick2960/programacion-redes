'''
    Descripción de la API: ExchangeRate-API
	Autor: Jose Ricardo Hernandez Vazquez 
	Fecha de creación: 30/Oct/2023

'''
import urllib.parse
import requests

while True:
    user_input = input("Presiona Enter para obtener el tipo de cambio USD a otras monedas o ingresa 'salir' para salir: ")

    if user_input.lower() == "salir":
        break  # Sale del bucle si el usuario ingresa "salir"

    url = 'https://exchangerate-api.p.rapidapi.com/rapid/latest/USD'
    headers = {
        'X-RapidAPI-Key': 'c0b8acd66fmshc7410b3a4886920p1adb72jsn7a2765ad01b0',
        'X-RapidAPI-Host': 'exchangerate-api.p.rapidapi.com'
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        json_data = response.json()
        print("Tipo de cambio USD a otras monedas:")
        for currency, rate in json_data['rates'].items():
            print(f"{currency}: {rate}")
    else:
        print(f"No se pudo obtener el tipo de cambio. Código de estado: {response.status_code}")

print("Saliendo del programa.")
