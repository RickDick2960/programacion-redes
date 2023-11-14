"""
Autor: Jose Ricardo Hernandez Vazquez
Fecha: 10 de noviembre de 2023
Descripción: Laboratorio 3.4.1.14
"""
import math

class Punto:
    def __init__(self, x=0.0, y=0.0):
        self.__x = x
        self.__y = y

    def obtener_x(self):
        return self.__x

    def obtener_y(self):
        return self.__y

    def distancia_desde_xy(self, x, y):
        return math.hypot(self.__x - x, self.__y - y)

    def distancia_desde_punto(self, punto):
        return math.hypot(self.__x - punto.obtener_x(), self.__y - punto.obtener_y())

punto1 = Punto(0, 0)
punto2 = Punto(1, 1)
print(punto1.distancia_desde_punto(punto2))
print(punto2.distancia_desde_xy(2, 0))
