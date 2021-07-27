#Tarea 52 - Ejercicio 1
#Autor: Daniel Bilbao
#Objetivo del primer ejercicio: 
#Desarrollar un programa que haga:
#- Solicitar al usuario que ingrese números, los cuales se guardarán en una lista. Finalizar al ingresar el número 0, el cual no debe guardarse.
#- A continuación, solicitar al usuario que ingrese un número y, si el número está en la lista, eliminar su primera ocurrencia. Mostrar un mensaje si no es posible eliminar.
#- Recorrer la lista para imprimir la sumatoria de todos los elementos.
#- Solicitar al usuario otro número y crear una lista con los elementos de la lista original que sean menores que el número dado. Imprimir esta nueva lista, iterando por ella.
#- Generar e imprimir una nueva lista que contenga como elementos a tuplas de dos elementos, cada una compuesta por un número de la lista original 
#y la cantidad de veces que aparece en ella. Por ejemplo, si la lista original es [5,16,2,5,57,5,2] la nueva lista contendrá: [(5,3), (16,1), (2,2), (57,1)]

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
            x=input("Introduce un numero entero:")

def MostrarLista(lista):
    """Funcion para mostrar por consola una lista
    Parametros:
        -lista: Lista a mostrar por pantalla
    Return:
        -Muestra por consola la lista introducida como agumento
    """
    print("\nA CONTINUACION SE MUESTRA LA LISTA:")
    for i in range(len(lista)):
        print("El elemento "+str(i+1)+" es:"+str(lista[i]))

def SolicitarNumeros():
    """Funcion que almacena los numeros introducidos por el usuario en una lista. Se dejan de ingresar numeros a la lista al añadir el 0
    Return:
        -Devuelve la lista de numeros enteros creada por el usuario
    """
    print("********************************PRIMER APARTADO********************************")
    print("A continuacion, introduzca numeros para llenar la lista ('0' para finalizar):")
    lista=[]
    numero=ValidarEntero(input("Introduce un numero entero:"))
    while numero!=0:
        lista.append(numero)
        numero=ValidarEntero(input("Introduce un numero entero:"))
    MostrarLista(lista)
    return lista

def EliminarPrimeraOcurrencia(lista):
    """Funcion que elimina la primera ocurrencia de un numero introducido por el usuario en la lista introducida como argumento. En caso de no ser posible, muestra un mensaje de ERROR por consola
    Parametros:
        -lista: Lista a modificar en funcion del numero introducido por el usuario
    Return:
        - Devuelve la lista modificada
    """
    print("\n********************************SEGUNDO APARTADO********************************")
    NumeroAEliminar=ValidarEntero(input("Introduzca el numero que desea eliminar de la lista:"))
    if NumeroAEliminar in lista:
        lista.remove(NumeroAEliminar)
    else:
        print("ERROR. El numero introducido no se encuentra en la lista!")
    MostrarLista(lista)

def Sumatoria (lista):
    """Funcion que recorre la lista y calcula la sumatoria de los elementos que contiene
    Parametros:
        -lista: Lista a recorrer
    Return:
        -Devuelve el resultado de la sumatoria de los numeros almacenados en la lista
    """
    print("\n********************************TERCER APARTADO********************************")
    sumatoria=0
    for i in lista:
        sumatoria=sumatoria+i
    print("El resultado de la sumatoria de los numeros almacenados en la lista es:"+str(sumatoria))

def CrearNuevaLista(lista):
    """Funcion que crea una nueva lista con los elementos de la lista original que sean menores que el número dado por el usuario. Además, se imprime esta nueva lista, iterando por ella.
    Parametros:
        lista: Lista a manipular
    Return:
        -Devuelve la nueva lista y la imprime por pantalla
    """
    print("\n********************************CUARTO APARTADO********************************")
    NuevaLista=[]
    print("A continuacion, se creara una lista con los elementos de la lista original que sean menores que el número dado por el usuario.")
    Numero=ValidarEntero(input("Introduce un numero entero:"))
    for i in range(len(lista)):
        if lista[i]<Numero:
            NuevaLista.append(lista[i])
    MostrarLista(NuevaLista)
    return NuevaLista

def GenerarListaTuplas(lista):
    """Funcion que gener una nueva lista que contiene como elementos tuplas de dos elementos, cada una compuerta por un numero de la lista original y a cantidad de veces que aparece
    Parametros:
        -lista: Lista a analizar
    Return:
        -Devuelve una lista de tuplas que contiene los numeros de la lista original y sus frecuencias de aparicion
    """
    print("\n********************************QUINTO APARTADO********************************")
    NuevaLista=[]
    for i in lista:
        if [i, lista.count(i)] not in NuevaLista:
            NuevaLista.append([i, lista.count(i)])
    MostrarLista(NuevaLista)
    return NuevaLista

def main():
    """Programa principal"""
    #Primer Apartado
    ListaNumeros=SolicitarNumeros()
    #Segundo Apartado
    EliminarPrimeraOcurrencia(ListaNumeros)
    #Tercer Apartado
    Sumatoria(ListaNumeros)
    #Cuarto Apartado
    CrearNuevaLista(ListaNumeros)
    #Quinto Apartado
    GenerarListaTuplas(ListaNumeros)

#endregion

if __name__=="__main__":
    main();