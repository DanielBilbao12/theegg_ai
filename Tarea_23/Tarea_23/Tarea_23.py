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

def GenerarBaraja():
    baraja=Baraja()
    baraja.mazo.append(Carta("A","Comodin"))
    baraja.mazo.append(Carta("B","Comodin"))
    return baraja

def MostrarBaraja(baraja):
    for carta in range(0,len(baraja.mazo),1):
        print("La carta numero "+str(carta+1)+" es "+str(baraja.mazo[carta]))

def BuscarComodines(mazo):
    indice=0
    for carta in mazo:
        if carta.valor == "Comodin" and carta.palo=="A":
            IndiceA=indice
            indice=indice+1
        elif carta.valor =="Comodin" and carta.palo=="B":
            IndiceB=indice
            indice=indice+1
        else:
            indice=indice+1
    return [IndiceA,IndiceB]

def MoverComodinA(indice,baraja):
    if indice==53 : #Si El comodin A esta en la ultima posicion, empezamos a contar desde arriba del mazo
        CartaComodinA=baraja.mazo[indice]
        baraja.mazo.pop(indice)
        indice=0
        baraja.mazo.insert(indice+1,CartaComodinA)
        MostrarBaraja(baraja)
    else:
        CartaComodinA= baraja.mazo[indice]
        baraja.mazo.pop(indice)
        baraja.mazo.insert(indice+1,CartaComodinA)
        MostrarBaraja(baraja)

def MoverComodinB(indice,baraja):
    if indice>51: #Si el comodin B esta en la penultima o ultima posicion, empezamos a contar desde arriba del mazo
        CartaComodinB=baraja.mazo[indice]
        baraja.mazo.pop(indice)
        indice=0
        baraja.mazo.insert(indice+1,CartaComodinB)
        MostrarBaraja(baraja)
    else:
        CartaComodinB= baraja.mazo[indice]
        baraja.mazo.pop(indice)
        baraja.mazo.insert(indice+2,CartaComodinB)
        MostrarBaraja(baraja)

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

def Solitario (baraja):
    #Encontrar comodinA y moverlo debajo de la carta que tiene debajo
    [IndiceComodinA,IndiceComodinB]=BuscarComodines(baraja.mazo)
    print("\nEl primer paso es cambiar el comodin A debajo de la carta que tiene debajo")
    MoverComodinA(IndiceComodinA,baraja)
    #Encontrar comodinB y moverlo por la carta de abajo de la que tiene debajo
    [IndiceComodinA,IndiceComodinB]=BuscarComodines(baraja.mazo)
    print("\nEl segundo paso es cambiar el comodin B por a carta de abajo de la que tiene debajo")
    MoverComodinB(IndiceComodinB,baraja)
    #Corto la baraja e intercambio las cartas encima del primer comodin por las de debajo del segundo comodin
    #Miro la ultima carta y cuento el numero que sea desde arriba
    #Una vez contado, corto la baraja dejando la carta de la ultima posicion tal y como esta
    #Observo la primera carta, cuento, y almaceno que carta es.--> Esta carta se convierte a letra y ya tenemos el primer caracter

def main():
    frase=input("Introduzca una frase a cifrar: ") #Esta es la frase que tenemos que cifrar
    frase=Cifrado1(frase)
    print(frase)
    baraja1=GenerarBaraja()
    MostrarBaraja(baraja1)
    #ristra=""
    #while len(frase)>len(ristra): #Mientras que la dimension de la ristra sea menor que la del mensaje a cifrar, generamos caracteres (Solitario)
    Solitario(baraja1) 

#endregion

main()