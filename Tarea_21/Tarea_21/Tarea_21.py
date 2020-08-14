# Tarea 21 
# Autor: Daniel Bilbao

#region
def mcd (numero1,numero2):
    """Funcion que calcula el maximo comun divisor (MCD) de dos numeros.
    Parametros:
        -n1: Un numero entero.
        -n2: Un numero entero.
    Return:
        -Devuelve el MCD.
    """
    aux=0
    while(numero2>0):
        aux=numero2
        numero2=numero1%numero2
        numero1=aux
    return numero1
def main():
    nUsuario=float(input())
    denominador=10000
    numerador=int(nUsuario*denominador)
    MCD=mcd(numerador,denominador)
    numerador=int(numerador/MCD)
    denominador=int(denominador/MCD)
    print(numerador,"/",denominador)
#endregion

main()