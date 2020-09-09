#Tarea 22
#Autor: Daniel Bilbao

from vaca import Vaca

#region
def ValidarEntero(x):
    """Funcion que valida si el valor introducido es Entero
    Parametros:
        -x: Valor introducido
    Return:
        -Devuelve el valor entero
    """
    while True:
        try:
            x=int(x)
            return x
        except ValueError:
            print("VALOR INCORRECTO")
            x=input("Introduce un valor entero positivo:")

def ValidarDecimal(x):
    """Funcion que valida si el valor introducido es Decimal
    Parametros:
        -x: Valor introducido
    Return:
        -Devuelve el valor decimal
    """
    while True:
        try:
            x=float(x)
            return x
        except ValueError:
            print("VALOR INCORRECTO")
            x=input("Introduce un valor numerico positivo:")

def MostrarVacasEnVenta(x):
    """Funcion que muestra un listado de las vacas en venta disponibles y sus estadisticas
    Parametros:
        -x: Lista de de objetos Vaca
    """
    print("\nA continuacion se muestra la lista de vacas y sus estadisticas")
    for i in range(len(x)):
        x[i].Info()

def CalculoDeProduccion(ListaVacas, CapacidadCamion, TotalProduccion, TotalPesoCamion, indice):
    """Funcion recursiva para calcular la Maxima producción que se puede obtener con las vacas en venta y la capacidad del camion
    Parametros:
        -ListaVacas: Lista de Objetos Vaca
        -CapacidadCamion: Peso que soporta el camion en kg
        -TotalProduccion: Cantidad de leche que se produce por dia en caso de llevarse el numero de vacas que se han analizado hasta el momento, su valor va cambiando
        -TotalPesoCamion: Cantidad de peso que lleva el camion en caso de llevarse el numero de vacas que se han analizadno hasta el momento, su valor va cambiando
    Return:
        - La produccion maxima que se puede obtener
    """
    if(indice<len(ListaVacas)): #Si todabia no hemos terminado de ver todas las posibilidades..
        VacaPosible=ListaVacas[indice] #Añado a la variable "VacaPosible" un objeto de la lista de vacas disponibles
        if(TotalPesoCamion+VacaPosible.peso>CapacidadCamion): #Si el peso que tiene ya el camion mas el peso de la vaca posible es mayor que la capacidad total del camion...
            #Opcion no valida, llamamos de nuevo a la funcion pero analizando la siguiente vaca
            return CalculoDeProduccion(ListaVacas,CapacidadCamion,TotalProduccion,TotalPesoCamion,indice+1)
        else:
            #Opcion valida, llamamos de nuevo a la funcion pero analizando la siguiente vaca teniendo en cuenta que cojemos la anterior y cojemos el resultado que de mas produccion de leche (con la anterior y sin la anterior)
            return max(CalculoDeProduccion(ListaVacas,CapacidadCamion,TotalProduccion+VacaPosible.produccion,TotalPesoCamion+VacaPosible.peso,indice+1),
                               CalculoDeProduccion(ListaVacas,CapacidadCamion,TotalProduccion,TotalPesoCamion,indice+1))
    return TotalProduccion

def RespuestaCorrecta(x):
    """Funcion para comprobar que la respuesta del usuario es SI o NO
    Parametros:
        -x= String
    Return:
        -Devuelve la respuesta SI o NO
    """
    while x.upper()!="NO" and x.upper()!="SI" :
        print("RESPUESTA INCORRECTA, RESPONDA CON UN SI O UN NO")
        x=input("¿Desea realizar otro analisis con vacas diferentes?")
    return x

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
    MostrarVacasEnVenta(VacasEnVenta)
    ProduccionMaxima=CalculoDeProduccion(VacasEnVenta,PesoCamion,0,0,0)
    print("\nLa producion maxima que se puede obtener es de: "+str(ProduccionMaxima)+" Litros")
#endregion

respuesta=""
while respuesta.upper()!="NO":
    main()
    respuesta=RespuestaCorrecta(input("¿Desea realizar otro analisis con vacas diferentes?"))