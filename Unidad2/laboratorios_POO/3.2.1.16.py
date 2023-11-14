"""
Autor: Jose Ricardo Hernandez Vazquez
Fecha: 10 de noviembre de 2023
Descripción: Laboratorio 3.2.1.16
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

    def esta_vacia(self):  
        return not bool(self.__cola)


class SuperCola(Cola):  
    pass


mi_super_cola = SuperCola()
mi_super_cola.agregar(1)
mi_super_cola.agregar("gato")  
mi_super_cola.agregar(True)   
for _ in range(4):
    if not mi_super_cola.esta_vacia():
        print(mi_super_cola.obtener())
    else:
        print("SuperCola vacía")
