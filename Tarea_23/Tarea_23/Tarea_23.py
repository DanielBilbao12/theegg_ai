# Tarea 23
# Autor: Daniel Bilbao

from Baraja import *

#Variable global para la conversion de NUMERO-LETRA
diccionario={1:"a",2:"b",3:"c",4:"d",5:"e",6:"f",7:"g",8:"h",9:"i",10:"j",11:"k",12:"l",13:"m",14:"n",15:"o",16:"p",17:"q",18:"r",19:"s",20:"t",21:"u",22:"v",23:"w",24:"x",25:"y",26:"z"}

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
        if carta.valor == "A" and carta.palo=="Comodin":
            IndiceA=indice
            indice=indice+1
        elif carta.valor =="B" and carta.palo=="Comodin":
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

def CortarEntreComodines(baraja):
    [IndiceComodinA, IndiceComodinB]=BuscarComodines(baraja.mazo) #Localizo donde estan los comodines
    IndicePrimerComodin=min(IndiceComodinA,IndiceComodinB) #Primer comodin es el que tenga indice menor
    IndiceSegundoComodin=max(IndiceComodinA,IndiceComodinB) #Segundo comodin es el que tenga indice mayor
    PrimerTrozo=baraja.mazo[0:IndicePrimerComodin]
    TrozoMedio=baraja.mazo[IndicePrimerComodin:IndiceSegundoComodin+1]
    SegundoTrozo=baraja.mazo[IndiceSegundoComodin+1:len(baraja.mazo)]
    baraja.mazo=SegundoTrozo+TrozoMedio+PrimerTrozo
    print("\nLa baraja tras el corte entre comodines queda asi:")
    MostrarBaraja(baraja)

def CortarMirandoUltimaCarta(baraja):
    UltimaCarta=baraja.mazo[53]
    if UltimaCarta.palo=="Comodin": #Si la ultima carta es comodin, se deja la baraja igual
        print("\nComo la ultima carta es comodin, la baraja no cambia")
    else:
        ValorUltimaCarta=UltimaCarta.valor
        print("\nLa ultima carta del mazo es un "+str(UltimaCarta)+" por lo que su valor es de "+str(ValorUltimaCarta))
        ValorNumericoUltimaCarta=ConversionValorNumero(ValorUltimaCarta)
        PaloUltimaCarta=UltimaCarta.palo
        if PaloUltimaCarta=="Treboles":
            ValorAContar=ValorNumericoUltimaCarta
        elif PaloUltimaCarta=="Diamantes":
            ValorAContar=ValorNumericoUltimaCarta+13
        elif PaloUltimaCarta=="Corazones":
            ValorAContar=ValorNumericoUltimaCarta+26
        elif PaloUltimaCarta=="Picas":
            ValorAContar=ValorNumericoUltimaCarta+39
        PrimerTrozo=baraja.mazo[0:ValorAContar]
        TrozoMedio=baraja.mazo[ValorAContar:len(baraja.mazo)-1]
        SegundoTrozo=baraja.mazo[len(baraja.mazo)-1:]
        baraja.mazo=TrozoMedio+PrimerTrozo+SegundoTrozo
        MostrarBaraja(baraja)

def ObtenerCaracter(baraja):
    PrimeraCarta=baraja.mazo[0]
    ValorNumericoPrimeraCarta=ConversionValorNumero(PrimeraCarta.valor)
    if PrimeraCarta.palo=="Treboles":
        ValorAContar=ValorNumericoPrimeraCarta+0
    elif PrimeraCarta.palo=="Diamantes":
        ValorAContar=ValorNumericoPrimeraCarta+13
    elif PrimeraCarta.palo=="Corazones":
        ValorAContar=ValorNumericoPrimeraCarta+26
    elif PrimeraCarta.palo=="Picas":
        ValorAContar=ValorNumericoPrimeraCarta+39
    elif PrimeraCarta.palo=="Comodin": #Si es comodin se cuenta 53
        ValorAContar=53
    CartaCaracter=baraja.mazo[ValorAContar] 
    return CartaCaracter

def ConversionValorNumero(x):
    if x=="A":
        valor=1
    elif x=="2":
        valor=2
    elif x=="3":
        valor=3
    elif x=="4":
        valor=4
    elif x=="5":
        valor=5
    elif x=="6":
        valor=6
    elif x=="7":
        valor=7
    elif x=="8":
        valor=8
    elif x=="9":
        valor=9
    elif x=="10":
        valor=10
    elif x=="J":
        valor=11
    elif x=="Q":
        valor=12
    elif x=="K":
        valor=13
    return valor

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

def Cifrado2 (mensaje,baraja):
    ristra=""
    while len(mensaje)>len(ristra): #Mientras que la dimension de la ristra sea menor que la del mensaje a cifrar, generamos caracteres (Solitario)
        for letra in mensaje:
                if letra!=" ":
                    ristra=ristra+Solitario(baraja)
                else:
                    ristra=ristra+" "
    print("\nLa ristra generada es la siguiente: "+str(ristra))
    return ristra

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
    CortarEntreComodines(baraja)
    #Miro la ultima carta y cuento el numero que sea desde arriba
    #Una vez contado, corto la baraja dejando la carta de la ultima posicion tal y como esta
    CortarMirandoUltimaCarta(baraja)
    #Observo la primera carta, cuento, y almaceno que carta es
    global ValorLetra
    Caracter=ObtenerCaracter(baraja)
    if Caracter.palo=="Comodin":
        Solitario(baraja) #APLICO RECURSIVIDAD
    #Convertir el caracter a letra, y ya esta "solitario"
    if Caracter.palo=="Diamantes" or Caracter.palo=="Picas":
        ValorLetra=ConversionValorNumero(Caracter.valor)+13
    elif Caracter.palo=="Treboles" or Caracter.palo=="Corazones":
        ValorLetra=ConversionValorNumero(Caracter.valor)+0
    for k,i in diccionario.items():
        if k==ValorLetra:
            Letra=diccionario[k]
    return Letra.upper()

def main():
    frase=input("Introduzca una frase a cifrar: ") #Esta es la frase que tenemos que cifrar
    #PRIMER PASO DEL CIFRADO
    frase=Cifrado1(frase)
    print(frase)
    baraja1=GenerarBaraja()
    print("\nLa baraja inicialmente esta asi:") #CUANTO TERMINE DE PROGRAMAR EL ALGORITMO CON ESTA CLAVE QUE HE DEFINIDO, MODIFICAR EL PROGRAMA PARA PEDIR CLAVE AL USUARIO Y BARAJAR RESPECTO A ESA CLAVE
    MostrarBaraja(baraja1)
    #SEGUNDO PASO DEL CIFRADO
    Ristra=Cifrado2(frase,baraja1)
    #TERCER PASO DEL CIFRADO--> SUMAR FRASE Y RISTRA
    #PRIMERO: CONVERTIR FRASE A NUMEROS

    #SEGUNDO: CONVERTIR RITRA A NUMEROS
    #TERCERO: SUMARLO Y CONVERTIR EL RESULTADO DE CADA SUMA A LETRA, JUNTARLAS EN UNA FRASE, Y TEXTO CIFRADO
#endregion

main()