# Tarea 23
# Autor: Daniel Bilbao

from Baraja import *

#region
def DividirCadena(cadena, separador, numeroCaracteres):
    """Funcion que divide una cadena (string) cada x caracteres y le añade el separador que se le indique
    Parametros:
        -cadena: String que se quiere separar
        -separador: caracter que se quiere usar como separador
        -numeroCaracteres: valor entero que define cada cuantos caracteres se le quiere añadir el separador a la cadena
    Return:
        - Devuelve la cadena separada por el separador cada x caracteres
    """
    frase = ""
    contador = 0
    for caracter in cadena:
        if contador == numeroCaracteres:
            frase += separador
            contador = 0
        contador += 1
        frase += caracter
    return frase

def Cifrado1 (mensaje): #Primer paso del cifrado, divide la frase en grupos de 5 letras y si hacen falta caracteres se le añade 'X' al final
    """Funcion que hace el primer paso para el cifrado
    Parametros:
        -mensaje: Mensaje a cifrar
    Return:
        -Devuelve la frase separada en cadenas de 5 caracteres y en caso de que falten caracteres para completar las cadenas, con 'X'-es añadidas
    """
    mensaje=mensaje.replace(" ","") #Le quito los espacios en blanco al mensaje
    while len(mensaje)%5 != 0: #Le añado 'X' en caso de que el mensaje no sea multiplo de 5
        mensaje+="X"
    mensaje=DividirCadena(mensaje," ",5) #Separo el string en cadenas de 5 caracteres
    return mensaje


def main():
    frase=input("Introduzca una frase a cifrar: ") #Esta es la frase que tenemos que cifrar
    print(Cifrado1(frase))
    baraja=Baraja()
    baraja.mazo.append(Carta("A","Comodin"))
    baraja.mazo.append(Carta("B","Comodin"))
    for carta in range(0,len(baraja.mazo),1):
        print("La carta numero "+str(carta+1)+" es "+str(baraja.mazo[carta]))
   
#endregion

main()