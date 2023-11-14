"""
Autor: Jose Ricardo Hernandez Vazquez
Fecha: 10 de noviembre de 2023
Descripción: Laboratorio 3.2.1.14
"""

class Pila:
    def __init__(self):
        self.__pila = []

    def push(self, valor):
        self.__pila.append(valor)

    def pop(self):
        valor = self.__pila[-1]
        del self.__pila[-1]
        return valor

class PilaContadora(Pila):
    def __init__(self):
        super().__init__() 
        self.__contador = 0  # Llena el constructor con acciones apropiadas.

    def obtener_contador(self):
        return self.__contador

    def pop(self):
        valor = super().pop() 
        self.__contador += 1 
        return valor  # Haz un pop y actualiza el contador.

pila_contadora = PilaContadora()
for i in range(100):
    pila_contadora.push(i)
    pila_contadora.pop()
print(pila_contadora.obtener_contador())
