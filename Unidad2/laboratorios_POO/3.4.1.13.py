"""
Autor: Jose Ricardo Hernandez Vazquez
Fecha: 10 de noviembre de 2023
Descripción: Laboratorio 3.4.1.13
"""
class ErrorDiaSemana(Exception):
    pass

class Semanero:
    DIAS_DE_LA_SEMANA = ['Lun', 'Mar', 'Mie', 'Jue', 'Vie', 'Sab', 'Dom']

    def __init__(self, dia):
        if dia not in self.DIAS_DE_LA_SEMANA:
            raise ErrorDiaSemana("Día de la semana no válido")
        self.__dia = dia

    def __str__(self):
        return self.__dia

    def agregar_dias(self, n):
        indice_actual = self.DIAS_DE_LA_SEMANA.index(self.__dia)
        nuevo_indice = (indice_actual + n) % 7
        self.__dia = self.DIAS_DE_LA_SEMANA[nuevo_indice]

    def restar_dias(self, n):
        indice_actual = self.DIAS_DE_LA_SEMANA.index(self.__dia)
        nuevo_indice = (indice_actual - n) % 7
        self.__dia = self.DIAS_DE_LA_SEMANA[nuevo_indice]

try:
    dia_semana = Semanero('Lun')
    print(dia_semana)
    dia_semana.agregar_dias(15)
    print(dia_semana)
    dia_semana.restar_dias(23)
    print(dia_semana)
    dia_semana = Semanero('Invalido')
except ErrorDiaSemana:
    print("Lo siento, no puedo atender tu solicitud.")
