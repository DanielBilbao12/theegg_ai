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
    print("El texto contiene "+str(caracteres)+" caracteres\n")

def CuentaPalabras(texto):
    """Funcion que cuenta el numero de palabras que contiene el texto
    Parametros:
        -texto: Texto a analizar
    Return:
        -Devuelve el numero de palabras que contiene el texto
    """



def FrecuenciaPalabras(ListaPalabras):
    """Funcion que devuelve la frecuencia con la que aparece cada una de las palabras en el texto
    Parametros:
        -ListaPalabras: Lista de las palabras que contiene el texto
    Return:
        -Devuelve la frecuencia de aparicion de las palabras del texto
    """
    
def main():
    """Funcion principal"""
    Texto=ExtraerTexto(input("Introduzca el nombre del archivo a analizar (Nombre.txt):"))
    CuentaCaracteres(Texto)

#endregion

if __name__ == "__main__":
    main()