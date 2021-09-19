cars = []
cantidad = len(cars)
hora = 2000

def parquear():
    if cantidad < 10:
        tiempo = int(input("cuanto horas desea parquear su auto: "))
        global cobro
        cobro = tiempo*hora
        global placa
        placa = input("ingrese los datos de su placa: ")
        cars.append(placa)
        puesto = cars.index(placa) + 1
        text = "su auto fue parqueado en el puesto N° {}"
        print(text.format(puesto))
    else:
        print("el parqueadero esta lleno, no podras ingresar")

def retirar():
    placa = input("ingrese los datos de su placa: ")
    if placa in cars:
        cars.remove(placa)
        texto = "usted debe pagar {} pesos por el parqueo de su auto"
        print(texto.format(cobro))

        print("adios y gracias por parquear en 'DEEP GARAGE'")
    else:
        print("su auto no ha ingresado a este parqueadero")

def estado():
    txt = "bienvenido a deep garage el precio de la hora es: {}, en estos momentos nuestro establecimiento se encuentra con {} vehiculos parqueados"
    print(txt.format(hora, len(cars)))

def bienvenida():
  
    print("BIENVENIDO A DEEP GARAGE")
    print("1.- ingresar auto")
    print("2.- retirar su auto")
    print("3.- precios y estado del parqueadero")
    opcion = int(input("ingresa tu opción: "))
    if opcion == 1:
        parquear()
        bienvenida()
    elif opcion == 2:
        retirar()
        bienvenida()
    elif opcion == 3:
        estado()
        bienvenida()
    else:
        bienvenida()

bienvenida()
