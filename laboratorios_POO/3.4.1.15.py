"""
Autor: Jose Ricardo Hernandez Vazquez
Fecha: 10 de noviembre de 2023
Descripción: Laboratorio 3.4.1.15
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

class Triangulo:
    def __init__(self, vertice1, vertice2, vertice3):
        self.__vertices = [vertice1, vertice2, vertice3]

    def perimetro(self):
        lado1 = self.__vertices[0].distancia_desde_punto(self.__vertices[1])
        lado2 = self.__vertices[1].distancia_desde_punto(self.__vertices[2])
        lado3 = self.__vertices[2].distancia_desde_punto(self.__vertices[0])
        return lado1 + lado2 + lado3

triangulo = Triangulo(Punto(0, 0), Punto(1, 0), Punto(0, 1))
print(triangulo.perimetro())
