'''
 Nombre: Jose Ricardo Hernandez Vazquez
 Grupo: GIR0541
 Fecha: 01 de octubre del 2023
 Ejercicio:3.4.1.13
'''

# Paso 1: Crear una lista vacía llamada beatles
beatles = []

# Paso 2: Agregar los miembros de la banda usando append()
beatles = ["John Lennon", "Paul McCartney", "George Harrison"]

# Paso 3: Pedir al usuario que agregue más miembros usando un bucle for y append()
miembros_add = ["Stu Sutcliffe", "Pete Best"]
for miembro in miembros_add :
    beatles.append(miembro)

# Paso 4: Eliminar a Stu Sutcliffe y Pete Best usando del
del beatles[3]  
del beatles[3]  

# Paso 5: Agregar a Ringo Starr al principio de la lista usando insert()
beatles.insert(0, "Ringo Starr")

# Imprimir la lista final
print(beatles)

# Probando la longitud de la lista
print("Número de miembros de los Beatles:", len(beatles))
