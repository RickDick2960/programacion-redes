"""
Autor: Jose Ricardo Hernandez Vazquez
Fecha: 10 de noviembre de 2023
Descripción: Laboratorio 3.2.1.15
"""
class MiErrorDeCola(Exception):  
    pass


class Cola:
    def __init__(self):
        self.__cola = []

    def agregar(self, elemento):
        self.__cola.insert(0, elemento)

    def obtener(self):
        if not self.__cola:
            raise MiErrorDeCola("La cola está vacía")
        return self.__cola.pop()


mi_cola = Cola()
mi_cola.agregar(1)
mi_cola.agregar("gato")  
mi_cola.agregar(True)   
try:
    for _ in range(4):
        print(mi_cola.obtener())
except MiErrorDeCola:
    print("¡Error de Cola!")
