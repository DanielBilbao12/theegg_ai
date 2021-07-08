#Tarea 41
#Autor: Daniel Bilbao
#Objetivo: Ordenar de menor a mayor, buscar el numero 874 y realizar el analisis en Notacion Big O
# D la siguiente lista de elementos:  [3, 56, 21, 33, 874, 123, 66, 1000, 23, 45, 65, 56].

from time import time #Libreria para mostrar tiempo de ejecucion para cada algoritmo de busqueda

#region
def OrdenarLista(Lista):
    """Funcion que ordena de menor a mayor una lista de numeros
    Parametros:
        -Lista: Array de numeros enteros
    Return:
        -Devuelve la lista ordenada
    """
    ListaOrdenada=Lista
    for i in range((len(ListaOrdenada)-1)):
        if ListaOrdenada[i]>ListaOrdenada[i+1]:
            aux=ListaOrdenada[i]
            ListaOrdenada[i]=ListaOrdenada[i+1]
            ListaOrdenada[i+1]=aux
            OrdenarLista(ListaOrdenada) #Recursividad
    return ListaOrdenada

def MostrarLista(Lista):
    """Funcion que Muestra por pantalla la lista de numeros enteros
    Parametros:
        -Lista: Array de numeros enteros
    Return:
        -Printea por pantalla la lista
    """
    print("La lista es la siguiente:")
    for i in range(len(Lista)):
        print("Posicion "+str(i+1)+" :"+str(Lista[i]))

def BuscarNumero_Secuencial(numero, Lista):
    """Funcion que busca un numero en una lista de forma secuencial
    Parametros:
        -numero: Numero a buscar
        -Lista: Array de numeros enteros donde hay que buscar el numero
    Return:
        -Muestra por pantalla la posicion del numero en la lista, el numero de iteraciones necesarias para encontrar el numero, y el tiempo de ejecucion
    """
    t0=time()
    iteraciones=0
    for i in range(len(Lista)):
        iteraciones+=1
        if numero==Lista[i]:
            print("\nLos resultados con el algoritmo de busqueda secuencial son los siguientes:")
            print("     -Iteraciones con algoritmo de busqueda secuencial: "+str(iteraciones))
            print("     -El numero "+str(numero)+" se encuentra en la posicion: "+str(i+1))
            print("     -El algoritmo de busqueda secuencial ha tardado: %0.5f" %(time()-t0)+" segundos")
            break #Salgo del FOR
    if iteraciones==len(Lista):
        print("No se ha encontrado el numero "+str(numero)+" en la lista mediante la busqueda secuencial")


def BuscarNumero_Binaria(numero, lista):
    """Funcion que busca un numero en una lista de forma binaria
    Parametros:
        -numero: Numero a buscar
        -Lista: Array de numeros enteros donde hay que buscar el numero
    Return:
        -Muestra por pantalla la posicion del numero en la lista, el numero de iteraciones necesarias para encontrar el numero y el tiempo de ejecucion
    """
    t0=time()
    iteraciones=0
    izq = 0
    der = len(lista) -1 
    while izq <= der:
        medio = int((izq+der)/2)
        iteraciones+=1
        if lista[medio] == numero:
            print("\nLos resultados con el algoritmo de busqueda binaria son los siguientes:")
            print("     -Iteraciones con algoritmo de busqueda binaria: "+str(iteraciones))
            print("     -El numero "+str(numero)+" se encuentra en la posicion: "+str(medio+1))
            print("     -El algoritmo de busqueda binaria ha tardado: %0.5f" %(time()-t0)+" segundos")
            break #Salgo del bucle
        elif lista[medio] > numero:
            der = medio-1
        else:
            izq = medio+1
    if lista[medio]!=numero: #Condicion para saber si el numero estaba en la lista o no
        print("No se ha encontrado el numero "+str(numero)+" en la lista mediante la busqueda binaria")


def main():
    """Funcion principal"""
    ListaNumeros=[3, 56, 21, 33, 874, 123, 66, 1000, 23, 45, 65, 56] #Declaracion de la lista de numeros a ordenar
    ListaDeMenorAMayor=OrdenarLista(ListaNumeros) #Haciendo "sorted(ListaNumeros)" ya obtendriamos la lista ordenada pero se pide crear nuestro propio algoritmo
    MostrarLista(ListaDeMenorAMayor)
    BuscarNumero_Secuencial(874, ListaDeMenorAMayor)
    BuscarNumero_Binaria(874, ListaDeMenorAMayor)

#endregion

if __name__=="__main__":
    main()


