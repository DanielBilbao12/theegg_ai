#Tarea 41
#Autor: Daniel Bilbao
#Objetivo: Compresion y Descompresion LZ77 de una cadena de maximo 30 caracteres

#region
def ValidarString(frase):
    """Funcion que valida que el string introducido por el usuario es válido:
    Condiciones: 
        -Frase con un maximo de 30 caracteres comunes
    Parametros:
        -Frase: String introducido por el usuario
    Return:
        -Devuelve la frase correctamente introducida por el usuario
    """

    while len(frase)>30:
        print("ERROR. El String introducido debe tener un máximo de 30 caracteres y tiene "+str(len(frase))+" caracteres")
        frase=input("Introduzca el string a codificar (maximo 30 caracteres):")
    print("El tamaño del string introducido es de "+str(len(frase))+" caracteres")
    return frase

def Compresion (longitud_vent, longitud_Buff, frase):
    """Funcion que realiza la compresion del String mediante el algormito LZ77
    Parametros:
    ***********************FALTAN PARAMETROS POR DOCUMENTAR**********************
        -frase: String a comprimir
    Return:
        -Devuelve el string comprimido segun el algoritmo LZ77
    """
    length = longitud_Buff #matched length=0
    win = longitud_vent #window length=10?¿
    pointer = 0 #Pointer, initially pointing to the first position
    message = frase #coding information
    compressed_message = list() #Use tuple storage
    while True:
        if pointer - win < 0:
            match = message[0:pointer]
        else:
            match = message[pointer - win:pointer]
        while match.find(message[pointer:pointer + length + 1]) != -1:
            length += 1
        first = match.find(message[pointer:pointer + length])
        if pointer - win > 0:
            first += pointer - win
        if length != 0:
            a = (pointer - first, length, message[pointer + length])
            compressed_message.append(a)
            pointer += length + 1
        else:
            b = (0,0,message[pointer])
            compressed_message.append(b)
            pointer +=1
        length = 0
        if pointer == len(message):
            break
    print("El resultado de la compresion es", end=" ")
    for i, j, k in compressed_message:
        print(k, end="")
    print("\nEl tamaño del string comprimido es de "+str(len(compressed_message))+" caracteres")
    return compressed_message

def Descompresion (str_comprimido):
    """Funcion que realiza la descompresion del String comprimido mediante el algoritmo LZ77
    Parametros:
    ***************FALTA POR COMENTAR**********************
        -str_comprimido: String comprimido mediante el algoritmo LZ77
    Return:
        -Devuelve el string descomprimido asociado al string comprimido introducido como argumento a la funcion
    """
    de_msg = ""
    for s in str_comprimido:
        if s[0] != 0:
            de_msg += de_msg[(len(de_msg) - s[0]): (len(de_msg) - s[0] + s[1])]
        de_msg += s[2]
    print("El resultado de la descompresion es "+str(de_msg))
    print("El tamaño del string comprimido es de "+str(len(de_msg))+" caracteres")
    return de_msg

def main():
    """Funcion principal"""
    Frase=ValidarString(input("Introduzca el string a codificar (maximo 30 caracteres):"))
    Comprimido=Compresion(10, 0, Frase) #Longitud de la ventana?¿?¿?¿?¿ hay casos que no funciona.
    Descomprimido=Descompresion(Comprimido)

#endregion

if __name__=="__main__":
    main()
