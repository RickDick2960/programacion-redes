'''
Autor: Hernandez Vazquez Jose Ricardo
Fecha: 1 Octubre 2023
Descripcion: Laboratorio 3.2.1.14
'''
blocks = int(input("Ingresa el número de bloques: "))

alt = 0
block_altura= 0  
block_cap = 1  
while block_altura + block_cap <= blocks:
    alt += 1 
    block_altura += block_cap
    block_cap += 1  
print("La altura de la pirámide es:", alt)