'''
    Descripción de la API: DroneDeploy
	Autor: Jose Ricardo Hernandez Vazquez 
	Fecha de creación: 30/Oct/2023

'''
import urllib.parse
import requests

base_url = 'https://free-nba.p.rapidapi.com/players/'

while True:
    try:
        player_number = input("Ingresa el número de jugador o escribe 'Salir' para terminar: ")

        if player_number.lower() == 'salir':
            break

        # Construir la URL con el número de jugador ingresado por el usuario
        url = f'{base_url}{player_number}'

        headers = {
            'X-RapidAPI-Key': 'c0b8acd66fmshc7410b3a4886920p1adb72jsn7a2765ad01b0',
            'X-RapidAPI-Host': 'free-nba.p.rapidapi.com'
        }
        response = requests.get(url, headers=headers)

        status_code = response.status_code
        if status_code == 200:
            data = response.json()
            print(data)
        else:
            print(f'Código de estatus: {status_code}')

    except requests.exceptions.RequestException as err:
        print(f'Error al realizar la solicitud: {err}')
json_data = requests.get(url).json()