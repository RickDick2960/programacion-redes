'''
Jose Ricardo Hernandez Vazquez
01 de Octubre del 20203
Descripcion:  u1_prob1

'''

monto_depositado = float(input("Ingrese la cantidad de dinero depositada: "))

tasa_interes = 0.04

ahorros_despues_del_primer_anio = monto_depositado * (1 + tasa_interes)
ahorros_despues_del_segundo_anio = ahorros_despues_del_primer_anio * (1 + tasa_interes)
ahorros_despues_del_tercer_anio = ahorros_despues_del_segundo_anio * (1 + tasa_interes)

ahorros_despues_del_primer_anio = round(ahorros_despues_del_primer_anio, 2)
ahorros_despues_del_segundo_anio = round(ahorros_despues_del_segundo_anio, 2)
ahorros_despues_del_tercer_anio = round(ahorros_despues_del_tercer_anio, 2)

print(f"Ahorros después del primer año: {ahorros_despues_del_primer_anio}")
print(f"Ahorros después del segundo año: {ahorros_despues_del_segundo_anio}")
print(f"Ahorros después del tercer año: {ahorros_despues_del_tercer_anio}")