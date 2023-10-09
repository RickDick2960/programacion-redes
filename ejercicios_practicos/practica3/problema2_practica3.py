'''
 Nombre: Jose Ricardo Hernandez Vazquez
 Grupo: GIR0541
 Fecha: 09 de octubre del 2023
 Asignatura: Programacio  de redes.
 Ejercicios Practicos.
'''
lstnombres = []

for i in range(5):
    nombre_amigo = input("Ingresa el nombre de un amig@: ")
    lstnombres.append(nombre_amigo)

lstedades = []

for i in range(5):
    edad_amigo = input("Ingresa la edad de " + lstnombres[i] + ":")
    lstedades.append(edad_amigo)

dicDatos = {}
for i in range(5):
    dicDatos[lstnombres[i]] = lstedades[i]

def mostrar_diccionario(dic):
    for nombre, edad in dic.items():
        print(nombre, "->", edad)

print("Contenido del diccionario:")
mostrar_diccionario(dicDatos)

print("Longitud de lstnombres:", len(lstnombres))
print("Longitud de lstedades:", len(lstedades))
print("Tamaño de dicDatos:", len(dicDatos))

claves_ordenadas = sorted(dicDatos.keys())
print("Claves ordenadas:", claves_ordenadas)

 
def buscar_en_diccionario(dic, clave):
    if clave in dic:
        return dic[clave]
    else:
        return None
    
clave_buscar = input("Ingrese un nombre para buscar en el diccionario: ")
resultado_busqueda = buscar_en_diccionario(dicDatos, clave_buscar)
if resultado_busqueda is not None:
    print(clave_buscar, ":", resultado_busqueda)
else:
    print(clave_buscar, "no encontrado en el diccionario.")
