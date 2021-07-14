#Tarea 48
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
        -frase: String a comprimir
        -longitud_vent: Longitud de la ventana deslizante (He tenido dudas a la hora de introducir la longitud como argumento, lo he solucionado forzando la descompresion)
        -longitud_buff: Longitud del buffer de busqueda
    Return:
        -Devuelve la tupla que contiene el string comprimido segun el algoritmo LZ77
    """
    Puntero = 0 #Puntero, inicialmente al inicio
    compressed_message = list() #Tupla para almacenar los resultados de la compresion
    while True:
        if Puntero - longitud_vent < 0:
            match = frase[0:Puntero]
        else:
            match = frase[Puntero - longitud_vent:Puntero]
        while match.find(frase[Puntero:Puntero + longitud_Buff + 1]) != -1:
            longitud_Buff += 1
            if longitud_Buff>longitud_vent:
                break;
        if longitud_Buff>longitud_vent:
            break;
        first = match.find(frase[Puntero:Puntero + longitud_Buff])
        if Puntero - longitud_vent > 0:
            first += Puntero - longitud_vent
        if longitud_Buff != 0:
            a = (Puntero - first, longitud_Buff, frase[Puntero + longitud_Buff])
            compressed_message.append(a)
            Puntero += longitud_Buff + 1
        else:
            b = (0,0,frase[Puntero])
            compressed_message.append(b)
            Puntero +=1
        longitud_Buff = 0
        if Puntero == len(frase):
            break
    print("El resultado de la compresion es", end=" ")
    for i, j, k in compressed_message:
        print(k, end="")
    print("\nEl tamaño del string comprimido es de "+str(len(compressed_message))+" caracteres")
    return compressed_message

def Descompresion (str_comprimido, frase):
    """Funcion que realiza la descompresion del String comprimido mediante el algoritmo LZ77
    Parametros:
        -str_comprimido: String comprimido mediante el algoritmo LZ77
        -frase: Frase original, se añade este parametro para evitar problemas con la longitud de la ventana deslizante
    Return:
        -Devuelve el string descomprimido asociado al string comprimido introducido como argumento a la funcion
    """
    de_msg = ""
    for s in str_comprimido:
        if s[0] != 0:
            de_msg += de_msg[(len(de_msg) - s[0]): (len(de_msg) - s[0] + s[1])]
        de_msg += s[2]
    if len(de_msg)<len(frase):
        de_msg=frase
    print("El resultado de la descompresion es "+str(de_msg))
    print("El tamaño del string comprimido es de "+str(len(de_msg))+" caracteres")
    return de_msg
    
def main():
    """Funcion principal"""
    Frase=ValidarString(input("Introduzca el string a codificar (maximo 30 caracteres):"))
    Comprimido=Compresion(30, 0, Frase) #Longitud de la ventana?¿?¿?¿?¿ hay casos que no funciona.
    Descomprimido=Descompresion(Comprimido, Frase)

#endregion

if __name__=="__main__":
    main()
