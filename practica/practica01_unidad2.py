'''
    Descripción de la API: Currency Exchang
	Autor: Jose Ricardo Hernandez Vazquez 
	Fecha de creación: 30/Oct/2023

'''
import urllib.parse
import requests

url = 'https://currency-exchange.p.rapidapi.com/exchange'
headers = {
    'X-RapidAPI-Key': 'c0b8acd66fmshc7410b3a4886920p1adb72jsn7a2765ad01b0',
    'X-RapidAPI-Host': 'currency-exchange.p.rapidapi.com'
}

while True:
    to_currency = input("Introduce la moneda a la que quieres convertir (por ejemplo, MYR): ")
    from_currency = input("Introduce la moneda de origen (por ejemplo, SGD): ")
    amount = input("Introduce la cantidad a convertir (por ejemplo, 1.0): ")

    params = {
        'to': to_currency,
        'from': from_currency,
        'q': amount
    }

    try:
        response = requests.get(url, headers=headers, params=params)
        data = response.json()
        print(f"Resultado de la conversión: {data}")
    except Exception as error:
        print(f"Error en la conversión: {error}")

    salir= input("¿Necesitas otra divisa? : (Salir 's' / Otra 'o')")
    if salir.lower() != 'o':
        break
    json_data = requests.get(url).json()