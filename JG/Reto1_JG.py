lunes, martes, miercoles = 2.00
jueves, viernes =2.50
sabado, domingo = 3.00
precio = 0
tiempocliente = int(input("Ingrese su tiempo en minutos: "))
diacliente = str(input("Escriba el dia: "))
if tiempocliente >= 5 :
    if diacliente == lunes or martes or miercoles:
        t= tiempocliente/60
        precio= t * diacliente
    if diacliente == jueves or viernes:
        t= tiempocliente/60
        precio= t * diacliente
    if diacliente == sabado or domingo:
        t = tiempocliente/60
        precio = t* diacliente
else :
    print("No tienes deudas")

