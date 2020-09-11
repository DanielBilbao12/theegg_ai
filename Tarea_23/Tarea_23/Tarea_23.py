# Tarea 23
# Autor: Daniel Bilbao

#Declaracion de variables constantes
diccionario={"a":1,"b":2,"c":3,"d":4,"e":5,"f":6,"g":7,"h":8,"i":9,"j":10,"k":11,"l":12,"m":13,"n":14,"ñ":15,"o":16,"p":17,"q":18,"r":19,"s":20,"t":21,"u":22,"v":23,"w":24,"x":25,"y":26,"z":27}

#region
def Cifrado1 (mensaje): #Primer paso del cifrado, divide la frase en grupos de 5 letras y si hacen falta caracteres se le añade 'X' al final
    mensaje=mensaje.replace(" ","") #Le quito los espacios en blanco al mensaje
    while len(mensaje)%5 != 0: #Le añado 'X' en caso de que el mensaje no sea multiplo de 5
        mensaje+="X"
    #TENGO QUE SEPARAR EL STRING RELLENO CON LAS ´X´ EN GRUPOS DE 5...
    return mensaje
def main():
    frase=input("Introduzca una frase a cifrar: ") #Esta es la frase que tenemos que cifrar
    print(Cifrado1(frase))
#endregion

main()