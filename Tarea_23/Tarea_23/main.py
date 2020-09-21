# Tarea 23
# Autor: Daniel Bilbao

from Baraja import *

#Variables globales para la conversion de NUMERO-LETRA-NUMERO
diccionario={1:"a",2:"b",3:"c",4:"d",5:"e",6:"f",7:"g",8:"h",9:"i",10:"j",11:"k",12:"l",13:"m",14:"n",15:"o",16:"p",17:"q",18:"r",19:"s",20:"t",21:"u",22:"v",23:"w",24:"x",25:"y",26:"z"}
diccionario2={"a":1,"b":2,"c":3,"d":4,"e":5,"f":6,"g":7,"h":8,"i":9,"j":10,"k":11,"l":12,"m":13,"n":14,"o":15,"p":16,"q":17,"r":18,"s":19,"t":20,"u":21,"v":22,"w":23,"x":24,"y":25,"z":26}

#region
def ValidarCadena (string):
    while string.
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
    """Funcion que genera una baraja ordenada de A a K (TREBOLES, DIAMANTES, CORAZONES Y PICAS) y el comodin A y B como ultimas cartas de la baraja
    Return
        - Devuelve la baraja
    """
    baraja=Baraja()
    baraja.mazo.append(Carta("A","Comodin"))
    baraja.mazo.append(Carta("B","Comodin"))
    return baraja

def MostrarBaraja(baraja):
    """Funcion que muestra la disposicion de la baraja
    Parametros:
        -baraja: Variable que almacena la baraja
    """
    for carta in range(0,len(baraja.mazo),1):
        print("La carta numero "+str(carta+1)+" es "+str(baraja.mazo[carta]))

def BuscarComodines(mazo):
    """Funcion que localica las posiciones de los comodines en la baraja
    Parametros:
        -mazo: Variable que almacena el mazo que compone la baraja
    Return:
        -Devuelve los indices del comodin A y comodin B respectivamente
    """
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
    """Funcion que mueve el comodin A debajo de la carta que tiene debajo
    Parametros:
        -indice: Posicion en la baraja del comodin A
        -baraja: Variable que almacena la baraja
    """
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
    """Funcion que mueve el comodin B debajo de la segunda carta que tiene debajo
    Parametros:
        -indice: Posicion en la baraja del comodin B
        -baraja: Variable que almacena la baraja
    """
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
    """Funcion que corta la baraja entre el primer comodin y el segundo comodin
    Parametros:
        -baraja: Variable que almacena la barajs
    """
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
    """Funcion que corta la baraja dependiendo de la ultima carta de la misma, dejando la ultima carta estatica
    Parametros:
        -baraja: Variable que almacena la baraja
    """
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

def OrdenarSegunClave(baraja,clave):
    #Convierto la clave en un array de numeros
    ClaveNumerica=[]
    for letra in clave:
        for k,v in diccionario2.items():
            if k.upper()==letra.upper():
                ClaveNumerica.append(diccionario2[k])
    #Con la clave convertida a numeros dentro de la lista, corto la baraja contando esos numeros
    for i in range(0,len(ClaveNumerica),1):
        ValorAContar=ClaveNumerica[i]
        PrimerTrozo=baraja.mazo[0:ValorAContar]
        TrozoMedio=baraja.mazo[ValorAContar:len(baraja.mazo)-1]
        SegundoTrozo=baraja.mazo[len(baraja.mazo)-1:]
        baraja.mazo=TrozoMedio+PrimerTrozo+SegundoTrozo

def ObtenerCaracter(baraja):
    """Funcion que obtiene el caracter correspondiente a la primera carta
    Parametros:
        -baraja: Variable que almacena la baraja
    Return:
        - Devuelve el objeto carta correspondiente al caracter
    """
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
    """Funcion para convertir el valor de la carta a un numero entero
    Parametros:
        -x: Valor de la carta a convertir
    Return:
        - Devuelve el valor numerico de la carta
    """
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

def Cifrado2 (mensaje,baraja,clave):
    """Funcion que hace el segundo paso del cifrado
    Parametros:
        -mensaje: Mensaje a cifrar
        -baraja: Variable que almacena la baraja
    Return:
        - Devuelve la ristra que se genera para el cifrado y descifrado del mensaje
    """
    ristra=""
    while len(mensaje)>len(ristra): #Mientras que la dimension de la ristra sea menor que la del mensaje a cifrar, generamos caracteres (Solitario)
        for letra in mensaje:
                if letra!=" ":
                    ristra=ristra+Solitario(baraja,clave)
                else:
                    ristra=ristra+" "
    print("\nLa ristra generada es la siguiente: "+str(ristra))
    return ristra

def Cifrado3(mensaje,ristra):
    """Funcion que hace el tercer paso del cifrado
    Parametros:
        -mensaje: Mensaje a cifrar
        -baraja: Variable que almacena la baraja
    Return:
        -Devuelve el mensaje cifrado, la ristra de forma numerica y el mensaje cifrado de forma numerica
    """
    #PRIMERO: CONVERTIR FRASE A NUMEROS
    FraseNumerica=[]
    for letra in mensaje: #Para cada letra en la frase
        for k,v in diccionario2.items(): #Miro el diccionario
            if k.upper()==letra.upper(): #Si el diccionario contiene la letra
                FraseNumerica.append(diccionario2[k])
    #SEGUNDO: CONVERTIR RISTRA A NUMEROS
    RistraNumerica=[]
    for letra in ristra:
        for k,v in diccionario2.items():
            if k.upper()==letra.upper():
                RistraNumerica.append(diccionario2[k])
    #TERCERO: SUMARLO LA RISTRANUMERICA Y LA FRASENUMERICA
    CifradoNumerico=[]
    for i in range(0,len(FraseNumerica),1):
        if FraseNumerica[i]+RistraNumerica[i]>26:
            CifradoNumerico.append(FraseNumerica[i]+RistraNumerica[i]-26)
        else:
            CifradoNumerico.append(FraseNumerica[i]+RistraNumerica[i])
    #CUARTO: CONVERTIR CIFRADONUMERICO A LETRAS Y ¡MENSAJE CIFRADO!
    MensajeCifrado=""
    for i in range(0, len(CifradoNumerico),1):
        for k,v in diccionario.items():
            if k==CifradoNumerico[i]:
                MensajeCifrado+=diccionario[k]
    MensajeCifrado=DividirCadena(MensajeCifrado," ",5)
    return [MensajeCifrado,RistraNumerica,CifradoNumerico]

def Descifrado1(CifradoNumerico, RistraNumerica):
    """Funcion que se encarga de descifrar el mensaje cifrado
    Parametros:
        -CifradoNumerico: Mensaje cifrado de forma numerica
        -RistraNumerica: Ristra de forma numerica
    Return:
        - Devuelve el mensaje descifrado
    """
    DescifradoNumerico=[]
    for i in range(0,len(CifradoNumerico),1):
        if CifradoNumerico[i]-RistraNumerica[i]<0:
            DescifradoNumerico.append(CifradoNumerico[i]-RistraNumerica[i]+26)
        else:
            DescifradoNumerico.append(CifradoNumerico[i]-RistraNumerica[i])
    #UNA VEZ TENGO LA RESTA DE FORMA NUMERICA, CONVERTIR A LETRAS Y MENSAJE DESCIFRADO!
    MensajeDescifrado=""
    for i in range(0, len(DescifradoNumerico),1):
        for k,v in diccionario.items():
            if k==DescifradoNumerico[i]:
                MensajeDescifrado+=diccionario[k]
    MensajeDescifrado=DividirCadena(MensajeDescifrado," ",5)
    return MensajeDescifrado

def Solitario (baraja, clave):
    """Funcion para aplicar solitario a la baraja
    Parametros:
        -baraja: Variable que almacena la baraja
    Return:
        - Devuelve la letra que se genera cada vez que se aplica solitario
    """
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
        Solitario(baraja,clave) #APLICO RECURSIVIDAD
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
    Frase=input("Introduzca una frase a cifrar: ") #Esta es la frase que tenemos que cifrar
    Clave=input("Introduzca una clave (En caso de que no se introduzca nada se utilizara la baraja por defecto tanto para el emisor como para el receptor):")
    #CIFRADO
    #PRIMER PASO DEL CIFRADO
    Frase=Cifrado1(Frase)
    print(Frase)
    baraja1=GenerarBaraja()
    if Clave!="": #Si se introduce una clave, ordenamos la baraja siguiendo la clave
        OrdenarSegunClave(baraja1,Clave)
    #SEGUNDO PASO DEL CIFRADO
    Ristra=Cifrado2(Frase,baraja1,Clave)
    #TERCER PASO DEL CIFRADO--> SUMAR FRASE Y RISTRA
    [Cifrado,RistraNumeros,CifradoNumeros]=Cifrado3(Frase,Ristra)
    print("\nEl mensaje cifrado es el siguiente: "+str(Cifrado.upper()))

    #DESCIFRADO
    Descifrado=Descifrado1(CifradoNumeros,RistraNumeros)
    print("\nEl mensaje descifrado es el siguiente: "+str(Descifrado.upper()))
#endregion

main()