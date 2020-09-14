# Tarea 23
# Autor: Daniel Bilbao

#Declaracion de variables constantes
diccionario={"a":1,"b":2,"c":3,"d":4,"e":5,"f":6,"g":7,"h":8,"i":9,"j":10,"k":11,"l":12,"m":13,"n":14,"ñ":15,"o":16,"p":17,"q":18,"r":19,"s":20,"t":21,"u":22,"v":23,"w":24,"x":25,"y":26,"z":27}

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
    return cifra

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
def Cifrado2 (): #Segundo paso del cifrado, Generar una ristra mediante "Solitario" de misma longitud y disposicion que la frase a crifrar despues del primer paso.


def main():
    frase=input("Introduzca una frase a cifrar: ") #Esta es la frase que tenemos que cifrar
    print(Cifrado1(frase))
#endregion

main()