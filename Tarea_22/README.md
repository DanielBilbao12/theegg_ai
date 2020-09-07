# ENUNCIADO DE LA TAREA 22

Usted es un original empresario de Azkoitia, y tiene la brillante idea de abrir una tienda de la leche en la Plaza del pueblo. Como es una persona muy prudente, desea que la leche que vender� sea perfectamente natural y fresca, y por esa raz�n, va a traer unas san�simas vacas de desde Tolosa. Dispone de un cami�n con un cierto l�mite de peso, y un grupo de vacas disponibles para la venta. Cada vaca puede tener un peso distinto, y producir una cantidad diferente de leche al d�a. Debes elegir qu� vacas comprar y llevar en su cami�n, de modo que pueda maximizar la producci�n de leche, observando el l�mite de peso del cami�n.

1.- Para este prop�sito tienes que definir las siguientes entradas:

Entrada: N�mero total de vacas en la zona de Tolosa que est�n a la venta. 
Entrada: Peso total que el cami�n puede llevar. Entrada: Lista de pesos de las vacas. 
Entrada: Lista de la producci�n de leche por vaca, en litros por d�a.

2.- El algoritmo que programes tiene que calcular la siguiente salida:

Salida: Cantidad m�xima de producci�n de leche se puede obtener.


# PRIMERAS IDEAS

Lo primero, crear una clase "vacas" para poder jugar con sus atributos (masa, produccion...)

Despues, utilizar la recursividad para calcular la maxima produccion de leche

Y por ultimo, crear el main. De esta manera pedimos al usuario los datos de entrada (Vacas por tolosa, masa que soporta el camion, lista de pesos de las vacas, lista de producion (L/dia) por vaca)