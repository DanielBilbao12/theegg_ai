#Tarea 44
#Autor: Daniel Bilbao
#Resolucion del ejercicio siguiente (Complejidad de un algoritmo - Notacion Big O: https://www.youtube.com/watch?v=GD254Gotp-4
#Objetivo: Definir dos funciones para calular la suma del 1 a "n" numeros. Una de ellas sumando uno a uno cada numero
# y la otra aplicando la formula de la suma aritmetica de Gauss

import time

#region
def ValidarEntero(numero):
    """Funcion que valida si el valor introducido es un numero entero
    Parametros:
        -numero: Valor introducido por el usuario
    Return:
        -Devuelve el numero entero
    """
    while True:
        try:
            numero=int(numero)
            while int(numero)<0:
                print("EL VALOR INTRODUCIDO NO ES UN NUMERO ENTERO")
                numero=input("Introduce un valor entero positivo:")
            return numero
        except ValueError:
            print("EL VALOR INTRODUCIDO NO ES UN NUMERO ENTERO")
            numero=input("Introduce un valor entero positivo:")

def SumaLineal(n):
    """Funcion que realiza la suma lineal desde 1 hasta el numero n
    Parametros:
        -n: Ultimo numero de la suma, introducido por el usuario
    Return:
        -Devuelve el valor de la suma desde 1 hasta n
     """
    suma=0
    for i in range (n+1):
        suma=suma+i
    return suma

def SumaCte(n):
    """Funcion que realiza la suma usando la formula de Gauss desde 1 hasta el numero n
    Parametros:
        -n: Ultimo numero de la suma, introducido por el usuario
    Return:
        -Devuelve el valor de la suma desde 1 hasta n
    """
    return (n/2)*(n+1)
        
def main():
    """Funcion Principal"""
    cantidad=ValidarEntero(input("Introduce un valor entero positivo:"))
    for i in range(4):
        t0=time.time()
        suma1=SumaLineal(cantidad)
        t1=time.time()
        suma2=SumaCte(cantidad)
        t2=time.time()
        print("{}   -   {}".format(suma1, t1-t0))
        print("{}   -   {}".format(suma2, t2-t1))
        cantidad*=10 #Aumentando el numero final de la suma, mayor carga computacional.

#end region

if __name__ == "__main__":
    main()
