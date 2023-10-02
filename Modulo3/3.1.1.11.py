'''
 Nombre: Jose Ricardo Hernandez Vazquez
 Grupo: GIR0541
 Fecha: 01 de octubre del 2023
 Ejercicio: 3.1.1.11
'''
ingreso = float(input("Ingrese el ingreso anual en pesos: "))

limite_superior = 85528  
exencion_fiscal = 556.02  
tasa_impositiva_superior = 0.32  
impuesto_fijo_superior = 14839.02  

if ingreso <= limite_superior:
    impuesto = round(0.18 * ingreso - exencion_fiscal)
else:
    impuesto = round(impuesto_fijo_superior + tasa_impositiva_superior * (ingreso - limite_superior))
    
if impuesto < 0:
    impuesto = 0

print("El impuesto calculado es:", impuesto, "pesos")
