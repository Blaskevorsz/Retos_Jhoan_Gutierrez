import math

tarifas = {
    'lunes': 2.00,
    'martes': 2.00,
    'miercoles': 2.00,
    'jueves': 2.50,
    'viernes': 2.50,
    'sabado': 3.00,
    'domingo': 3.00
}

diacliente = input("Ingrese el día (lunes, martes, ..., domingo): ").lower()

if diacliente in tarifas:
    tarifa = tarifas[diacliente]
    tiempocliente = int(input("Ingrese el tiempo en minutos: "))
    tiempohoras = math.ceil(tiempocliente / 60)  #redondea al entero mas cercano
    precio = tiempohoras * tarifa
    print(f"El precio a pagar es de: {precio:.2f}.")
else:
    print("Ingrese nuevamente el dia.")
