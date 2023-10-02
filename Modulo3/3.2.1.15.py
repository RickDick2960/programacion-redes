'''
 Nombre: Jose Ricardo Hernandez Vazquez
 Grupo: GIR0541
 Fecha: 01 de octubre del 2023
 Descripcion: Ejercicios 3.2.1.15
'''

# Leer un número natural desde el usuario
c0 = int(input("Ingrese un número natural: "))

steps = 0

while c0 != 1:
    print(c0)
    if c0 % 2 == 0:
        c0 = c0 // 2
    else:
        c0 = 3 * c0 + 1
    steps += 1
print(c0)
print("pasos =", steps )
