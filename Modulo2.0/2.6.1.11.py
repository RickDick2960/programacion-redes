'''
 Nombre: Jose Ricardo Hernandez Vazquez
 Grupo: GIR0541
 Fecha: 01 de octubre del 2023
 Descripcion: Ejercicios 2.6.1.11
'''

# Ingresar la hora de inicio en horas y minutos
hour = int(input("Hora de inicio (horas): "))
mins = int(input("Minuto de inicio (minutos): "))

# Ingresar la duración del evento en minutos
dura = int(input("Duración del evento (minutos): "))

# Calcular la hora final y los minutos finales
hour_final = (hour + (mins + dura) // 60) % 24
mins_final = (mins + dura) % 60

# Imprimir el resultado
print(f"El evento terminará a las {hour_final:02}:{mins_final:02}")
