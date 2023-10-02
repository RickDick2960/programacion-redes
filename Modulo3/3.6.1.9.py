'''
 Nombre: Jose Ricardo Hernandez Vazquez
 Grupo: GIR0541
 Fecha: 01 de octubre del 2023
 Ejercicio:3.6.1.9
 
'''
my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]

# Crear una lista vacía para almacenar elementos únicos
unica_list = []

for num in my_list:
    if num not in unique_list:
        unica_list.append(num)
        
print("La lista con elementos únicos:")
print(unica_list)
