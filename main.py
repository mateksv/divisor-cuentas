import utilities, objetos, TAD_LISTA
from utilities import *
from TAD_LISTA import *
from objetos import *
tituloConsola("Dividir Gastos")
callHandler()
clear()
try:
    personas = createList()

    def altaPersona(cant):
        aux = 0
        while aux < cant:
            # Se establecen los datos del objeto
            print("="*20)
            nombre = input("Nombre: ")
            inversion = float(input("Inversion inicial: $"))
            diferencia = 0.00
            # Se crea un objeto 'Persona'
            persona = Persona(nombre, inversion, diferencia)
            # Se agrega el objeto en la coleccion de personas
            addToList(personas, persona)
            aux += 1

    # Pregunto el total y cant personas a añadir
    setTittle("  CARGA DE DATOS  ", "=")
    compra = float(input("Monto total pagado: $"))
    aDividir = int(input("A dividir entre: "))
    altaPersona(aDividir)


    # calculo el monto total que debe pagar cada uno
    cantIguales = round(compra/size(personas), 2)

    # defino la cantidad inicial antes de la suma
    cantInicial = 0.00

    for i in range(0, size(personas)):
        # sumo la cantidad de dinero acumulada
        cantInicial += float(Persona.getInversion(personas[i]))

    clear() # limpio pantalla

    vuelto = round(cantInicial - compra, 2)
    if vuelto < 0:
        print("\nError --> vuelto < 0\n La cantidad de dinero acumulado debe ser igual o mayor al gasto.\n") # si vuelto < 0, el dinero acumulado no es suficiente para pagar.
        input()
        exit(1)

    # genero un ticket
    setTittle("            TICKET           ", "=")
    print("Cant. dinero acumulado: $", cantInicial)
    print("Gasto total: $", compra)
    print("Gasto dividido entre:", aDividir)
    print("Cada uno paga: $", cantIguales)
    print("Vuelto: $", vuelto)


    for i in range(0, size(personas)):
        diferencia = 0.00
        # calculo la diferencia inversion - cantIguales para ver si se le debe dinero o debe dinero
        diferencia = round(float(Persona.getInversion(personas[i])) - cantIguales, 2)
        Persona.modDiferencia(personas[i], diferencia)
        print("="*29)
        Persona.getAll(personas[i])
    print("="*29)

except Exception as ex:
    clear()
    print("\n>>>>> ERROR >>>>>", ex)
    input()

input("\nPresione cualquier tecla para continuar...")
# version 1.7