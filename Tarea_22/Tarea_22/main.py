#Tarea 22
#Autor: Daniel Bilbao

from vaca import Vaca

#region
def ValidarEntero(x):
    while True:
        try:
            x=int(x)
            return x
        except ValueError:
            print("VALOR INCORRECTO")
            x=input("Introduce un valor entero positivo:")

def ValidarDecimal(x):
    while True:
        try:
            x=float(x)
            return x
        except ValueError:
            print("VALOR INCORRECTO")
            x=input("Introduce un valor numerico positivo:")

def main():
    VacasEnVenta=[]
    #Entrada 1
    TotalVacas=ValidarEntero(input("Introduce el numero de vacas en venta de TOLOSA:"))
    #Entrada 2
    PesoCamion=ValidarDecimal(input("Introduce el peso (kg) que puede soportar el camion:"))
    #Entradas 3 y 4
    for i in range(1, TotalVacas+1):
        peso=ValidarDecimal(input("Introduce el peso (kg) de la vaca numero "+str(i)+":"))
        produccion=ValidarDecimal(input("Introduce la produccion (L/dia) de la vaca numero "+str(i)+":"))
        VacaRegistrada=Vaca(peso,produccion,i)
        VacasEnVenta.append(VacaRegistrada)
#endregion

main()