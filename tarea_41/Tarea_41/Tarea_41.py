#Tarea 41
#Autor: Daniel Bilbao
#Objetivo: Obtener nº caracteres, nº palabras y ranking de palabras por frecuencia de uso de un texto

#!/usr/bin/env python
# -*- coding: utf-8 -*-

#La cabecera al principio me permite utilizar la codificacion utf-8 en los strings.

from re import * # Libreria para el manejo de expresiones regulares, importo todo el codigo del modulo

#region
def ExtraerTexto (ruta):
    """ Funcion para extraer el texto a analizar de un archivo de texto (.txt) en la misma ruta que el proyecto
    Parametros:
        -ruta: String del nombre del archivo a analizar
    Return:
        -El texto que contiene el archivo indicado
    """ 
    path=ruta
    while ruta.lower()!="texto.txt":
        print("ERROR. El archivo que contiene el texto a analizar en la ruta de este proyecto no se llama:"+str(ruta))
        ruta=input("Introduzca el nombre del archivo a analizar (Nombre.txt):")
    texto=open(ruta,'r',-1,'utf-8') #Abro el archivo en modo lectura (read)
    return texto.read().lower(); #Devuelvo el texto en minusculas

def CuentaCaracteres (text):
    """Funcion que cuenta el numero de caracteres que contiene el texto
    Parametros:
        -texto: Texto a analizar
    """
    caracteres=len(findall(r"\S", text)) #\S reconoce todos los caracteres menos espacios, se pone r"" para que python identifique la expresion y no los caracteres '\' y 'S'
    print("El texto contiene "+str(caracteres)+" caracteres")

def CuentaPalabras(texto):
    """Funcion que cuenta el numero de palabras que contiene el texto
    Parametros:
        -texto: Texto a analizar
    Return:
        -Devuelve la lista con las palabras que contiene el texto
    """
    palabras=findall(r"\b[a-zA-Zá-üÁ-Ü\d]+",texto) #Busca palabras--> Con \b se analizan los limites de las palabras, con [...] busca caracter dento de esos rangos(Permitiendo caracteres con tilde y dieresis), con \d admite conjuntos de numeros como palabras y con el +, coincide con uno o mas digitos dentro de ese rango
    print("El texto contiene "+str(len(palabras))+" palabras")
    return palabras

def FrecuenciaPalabras(Lista):
    """Funcion que devuelve la frecuencia con la que aparece cada una de las palabras en el texto
    Parametros:
        -Lista: Lista de las palabras que contiene el texto
    Return:
        -Devuelve la lista de palabras ordenadas por frecuencia de uso (Mas usadas..Menos usadas)
    """

    DiccionarioPalabras={} #Instancio el diccionario que almacenara la clave-valor de cada palabra
    for palabra in Lista:
        if palabra in DiccionarioPalabras: #Si la palabra (clave) ya esta en el diccionario, aumentamos en 1 su valor(aparicion)
            DiccionarioPalabras[palabra]+=1
        else:#Si la palabra no esta en el diccionario, al ser la primera aparicion, su valor a 1 (una aparicion)
            DiccionarioPalabras[palabra]=1 

    return DiccionarioPalabras

def OrdenarListaPalabras_PorFrecuencia(diccionario):
    """Funcion para ordenar el diccionario que almacena los pares palabra-nº de veces que aparece la misma
    Parametros:
        -Diccionario: Lista clave-valor que almacena los pares
     """
    import operator  # Importo el modulo operador para usar la funcion itemgetter()
    dic_ordenado=sorted(diccionario.items(), key=operator.itemgetter(1), reverse=True)
    print("La lista de palabras por frecuencia de aparicion es la siguiente:\n")
    for clave, valor in dic_ordenado:
        print("La palabra "+str({clave})+" aparece "+str({valor})+" veces")


def main():
    """Funcion principal"""
    Texto=ExtraerTexto(input("Introduzca el nombre del archivo a analizar (Nombre.txt):"))
    CuentaCaracteres(Texto)
    ListaDePalabras=CuentaPalabras(Texto)
    DiccionarioPalabras=FrecuenciaPalabras(ListaDePalabras)
    OrdenarListaPalabras_PorFrecuencia(DiccionarioPalabras)


#endregion

if __name__ == "__main__":
    main()