"""
Autor: Jose Ricardo Hernandez Vazquez
Fecha: 10 de noviembre de 2023
Descripción: Laboratorio 3.4.1.12
"""

class Reloj:
    def __init__(self, horas=0, minutos=0, segundos=0):
        self.__horas = horas
        self.__minutos = minutos
        self.__segundos = segundos

    def __str__(self):
        return f"{self.__formato_digito(self.__horas)}:{self.__formato_digito(self.__minutos)}:{self.__formato_digito(self.__segundos)}"

    def __formato_digito(self, digito):
        return f"0{digito}" if digito < 10 else str(digito)

    def siguiente_segundo(self):
        self.__segundos += 1
        if self.__segundos == 60:
            self.__segundos = 0
            self.__minutos += 1
            if self.__minutos == 60:
                self.__minutos = 0
                self.__horas += 1
                if self.__horas == 24:
                    self.__horas = 0

    def segundo_anterior(self):
        self.__segundos -= 1
        if self.__segundos == -1:
            self.__segundos = 59
            self.__minutos -= 1
            if self.__minutos == -1:
                self.__minutos = 59
                self.__horas -= 1
                if self.__horas == -1:
                    self.__horas = 23

reloj = Reloj(23, 59, 59)
print(reloj)
reloj.siguiente_segundo()
print(reloj)
reloj.segundo_anterior()
print(reloj)
