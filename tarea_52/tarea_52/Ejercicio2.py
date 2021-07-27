#Tarea 52 - Ejercicio 2
#Autor: Daniel Bilbao
#Objetivo del primer ejercicio: 
#Solicitar al usuario que ingrese los nombres de pila de los alumnos de nivel primario de una escuela, finalizando al ingresar "x". 
#A continuación, solicitar que ingrese los nombres de los alumnos de nivel secundario, finalizando al ingresar "x"
#- Informar los nombres de todos los alumnos de nivel primario y los de nivel secundario, sin repeticiones.
#- Informar qué nombres se repiten entre los alumnos de nivel primario y secundario.
#- Informar qué nombres de nivel primario no se repiten en los de nivel secundario.

#region
def SolicitarNombres(string):
    """Funcion que solcita nombres al usuario hasta que este introduce "x"
    Return:
        -Devuelve una lista con los nombres introducidos por el usuario
    """
    lista=[]
    print("A continuacion, rellena la lista de los alumnos de "+str(string)+":")
    nombre=input("Introduzca un nombre:")
    while nombre!="x":
        lista.append(nombre.upper())
        nombre=input("Introduzca un nombre:")
    return lista

def MostrarTodosLosNombres(listap, listas):
    """Funcion que muestra todos los nombres de los alumnos de primaria y secundaria sin repeticiones
    Parametros:
        -listap: Lista de nombres de alumnos de primaria
        -listas: Lista de nombres de alumnos de secundaria
    Return:
        -Muestra por pantalla todos los nombres de ambos cursos sin repeticiones
    """
    print("A continuacion, se muestran todos los nombres de ambos cursos, sin repeticiones:")
    for nombre in listap|listas:
        print(nombre)

def MostrarRepeticionesEntreCursos(listap, listas):
    """Funcion que muestra todos los nombres repetidos entre ambos cursos
    Parametros:
        -listap: Lista de nombres de alumnos de primaria
        -listas: Lista de nombres de alumnos de secundaria
    Return:
        -Muestra por pantalla los nombres que se repiten entre ambos cursos
    """
    print("A continuacion, se muestran los nombres repetidos entre ambos cursos:")
    for nombre in listap&listas:
        print(nombre)

def MostrarNoRepeticionesEntreCursos(listap, listas):
    """Funcion que muestra todos los nombres no repetidos entre ambos cursos
    Parametros:
        -listap: Lista de nombres de alumnos de primaria
        -listas: Lista de nombres de alumnos de secundaria
    Return:
        -Muestra por pantalla los nombres que no se repiten entre ambos cursos
    """
    print("A continuacion, se muestran los nombres de primaria no repetidos en secundaria:")
    for nombre in listap-listas: #Si se querrian los de nivel secundario, restar alreves (listas-listap) ya que si los elementos no son iguales, el resultado almacena el elemento del primer objeto
        print(nombre)


def main():
    """Programa principal"""
    ListaPrimaria=set(SolicitarNombres("primaria"))
    ListaSecundaria=set(SolicitarNombres("secundaria"))
    MostrarTodosLosNombres(ListaPrimaria, ListaSecundaria)
    MostrarRepeticionesEntreCursos(ListaPrimaria, ListaSecundaria)
    MostrarNoRepeticionesEntreCursos(ListaPrimaria, ListaSecundaria)


#endregion

if __name__=="__main__":
    main();