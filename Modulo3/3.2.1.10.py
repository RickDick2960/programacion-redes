'''
Nombre: Jose Ricardo Hernandez Vazquez
 Grupo: GIR0541
 Fecha: 01 de octubre del 2023
 Ejercicio: 3.2.1.10
'''


# Indicar al usuario que ingrese una palabra
# y asignarlo a la variable user_word.

for letter in user_word:
user_word = input("Ingrese una palabra: ")
user_word = user_word.upper()

letras_no_consumidas = ""

for letter in user_word:
    
    if letter in "AEIOU":
        continue
    letras_no_consumidas += letter

for letra in letras_no_consumidas:
    print(letra)
