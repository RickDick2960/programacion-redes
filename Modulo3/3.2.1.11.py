'''
 Nombre: Jose Ricardo Hernandez Vazquez
 Grupo: GIR0541
 Fecha: 25 de septiembre del 2023
 Descripcion: Ejercicio 3.2.1.11
'''
# Pedir al usuario que ingrese una palabra
user_word = input("Ingrese una palabra: ")

user_word = user_word.upper()
word_without_vowels = ""

for letter in user_word:
    
    if letter in "AEIOU":
       
        continue
   
    word_without_vowels += letter


print("La palabra sin vocales es:", word_without_vowels)
