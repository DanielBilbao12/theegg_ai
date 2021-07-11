#Tarea 41
#Autor: Daniel Bilbao
#Objetivo: Ordenar de menor a mayor, buscar el numero 874 y realizar el analisis en Notacion Big O
# D la siguiente lista de elementos:  [3, 56, 21, 33, 874, 123, 66, 1000, 23, 45, 65, 56].

from time import time #Libreria para mostrar tiempo de ejecucion para cada algoritmo de busqueda
import random #Libreria para generar numeros enteros aleatorios
import pandas as pd #Libreria para manejo de estructuras de datos
import matplotlib.pyplot as plt #Libreria para generar graficos

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
        -Devuelve el numero de iteraciones, para su uso en el analisis BigO
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
    if Lista[iteraciones-1]!=numero:
        print("No se ha encontrado el numero "+str(numero)+" en la lista mediante la busqueda secuencial")
    return iteraciones

def BuscarNumero_Binaria(numero, lista):
    """Funcion que busca un numero en una lista de forma binaria
    Parametros:
        -numero: Numero a buscar
        -Lista: Array de numeros enteros donde hay que buscar el numero
    Return:
        -Muestra por pantalla la posicion del numero en la lista, el numero de iteraciones necesarias para encontrar el numero y el tiempo de ejecucion
        -Devuelve el numero de iteraciones, para su uso en el analisis BigO
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
    return iteraciones

def ListaAleatoria(longitud):
    """Funcion que gnera una lista de numeros enteros de manera aleatoria
    Parametros:
        -longitud: Longitud de la lista de numeros aleatorios
    Return:
        -Devuelve una lista de tamaño "longitud" con numeros aleatorios
    """
    Lista=[]
    for i in range(longitud):
        numero=random.randint(0,1000) #Asigno entero aleatorio entre 0 y 1000
        Lista.append(numero)
    Lista=sorted(Lista)
    return Lista

def Plotear (Indice, Dataframe):
    """Funcion para generar los graficos segun los datos almacenados
    Parametros:
        -Indice: Indice a buscar en la lista
        -DataFrame: Estructura de datos que almacena los resultados del analisis BigO
    Return:
        -Genera en la ruta del proyecto los graficos del analisis BigO
    """
    ax = Dataframe.plot.scatter(x='Longitud', y='Iteraciones_secuencial',figsize=(6, 4), label="Busqueda Secuencial",color="DarkRed", title='Análisis BIG O',xlabel='Longitud', ylabel='Numero de iteraciones',fontsize=10, rot=0)
    Dataframe.plot.scatter(x='Longitud', y='Iteraciones_binario',xlabel='Longitud', ylabel='Numero de iteraciones',label="Busqueda Binaria", color="DarkBlue", ax=ax)
    plt.savefig('Grafico_bigO_%s.png' % Indice)

def Prueba_BigO(Indice):
    """Funcion para el analisis Big-O de los algoritmos de busqueda
    Parametros:
        -Indice: Indice a buscar en la lista
        -lista: Lista de numeros enteros
    Return:
        -Genera gráficos para comparar ambos algoritmos de ordenacion
    """
    dataframe = pd.DataFrame(columns=['Longitud', 'Iteraciones_secuencial', 'Iteraciones_binario'])
    for i in range(100):
            lista=ListaAleatoria(random.randint(100,500))
            numero=lista[int(len(lista)*Indice)]
            It_secuencial=BuscarNumero_Secuencial(numero,lista)
            It_binaria=BuscarNumero_Binaria(numero,lista)
            result = dict(Longitud=[len(lista)],Iteraciones_secuencial=It_secuencial,Iteraciones_binario=It_binaria)
            dataframe = dataframe.append(pd.DataFrame(result, index=None), ignore_index=True)
    Plotear(Indice, dataframe)


def main():
    """Funcion principal"""
    #RESOLUCION DEL EJERCICIO
    ListaNumeros=[3, 56, 21, 33, 874, 123, 66, 1000, 23, 45, 65, 56] #Declaracion de la lista de numeros a ordenar
    ListaDeMenorAMayor=OrdenarLista(ListaNumeros) #Haciendo "sorted(ListaNumeros)" ya obtendriamos la lista ordenada pero se pide crear nuestro propio algoritmo
    MostrarLista(ListaDeMenorAMayor)
    BuscarNumero_Secuencial(874, ListaDeMenorAMayor)
    BuscarNumero_Binaria(874, ListaDeMenorAMayor)
    #ANALISIS BIG-O --> Genero listas aleatorias de diferetnes tamaños, busco valores en las listas y almaceno los resultados
    #para graficarlos y analizar los algoritmos de busqueda desarrollados
    Prueba_BigO(0) #Busqueda en la primera posicion del array
    Prueba_BigO(0.5) #Busqueda en la mitad del Array
    Prueba_BigO(0.8) #Busqueda en la mitad superior del array

#endregion

if __name__=="__main__":
    main()


