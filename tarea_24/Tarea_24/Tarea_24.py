#Tarea 24
#Autor: Daniel Bilbao

#region
def ConversionBinaria (numero):
    """Funcion que convierne un valor entero en binario
    Parametros:
        -numero: Numero entero
    Return:
        -Valor binario
    """
    binario=[]
    while numero>0 :
        binario.append(str(numero%2))
        numero//=2
    binario.reverse()
    return "".join(binario)

def ValidarEntero(numero):
    """Funcion que valida que la entrada del usuario es un valor numerico entero
    Parametros:
        -numero: Numero introducido por el usuario
    Return:
        -Numero entero
    """
    while True:
        try:
            numero=int(numero)
            return numero
        except ValueError:
            print("ERROR. EL VALOR INTRODUCIDO DEBE SER UN NUMERO ENTERO")
            numero=input("Introduzca un valor entero para la conversion a binario:")

def RespuestaCorrecta (x):
    """Funcion para comprobar que la respuesta del usuario es SI o NO
    Parametros:
        -x= String
    Return:
        -Devuelve la respuesta SI o NO
    """
    while x.upper()!="NO" and x.upper()!="SI":
        print("RESPUESTA INCORRECTA, RESPONDA CON UN SI O UN NO")
        x=input("¿Desea realizar otra conversion a binario?")
    return x

def main():
    Numero=ValidarEntero(input("Introduzca un valor entero para la conversion a binario:"))
    Binario=ConversionBinaria(Numero)
    print ("El numero "+str(Numero)+" en binario se expresa como: "+str(Binario))
#endregion

respuesta=""
while respuesta.upper()!="NO":
    main()
    respuesta=RespuestaCorrecta(input("¿Desea realizar otra conversión a binario?"))