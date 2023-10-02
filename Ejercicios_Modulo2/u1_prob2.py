'''
Jose Ricardo Hernandez Vazquez 
01 de Octubre del 2023
Descripcion: u1_prob2

'''
# Crear una lista de asignaturas
asignaturas = ["Probabilidad y Estadística","Electrónica para IDC Física","Conexión de redes WAN",
               "Administración de servidores I","Programación de Redes","Inglés IV"]

notas = {}

for asignatura in asignaturas:
    nota = float(input(f"Ingrese la nota de la unidad I de {asignatura}: "))
    notas[asignatura] = nota

for asignatura, nota in notas.items():
    print(f"En {asignatura} has sacado {nota}")
