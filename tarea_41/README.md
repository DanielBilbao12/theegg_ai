# ENUNCIADO DE LA TAREA 41

Para esta tarea se propone que el alumno mediante tecnicas Regex calcule el numero de caracteres, el numero de palabras y el ranking de palabras por frecuencia de uso del siguiente texto:

"En Strandhill, Irlanda, se cruz� en mi camino Chris, un se�or de los que inspiran y se posicionan como
referente. Fue una pieza fundamental en un momento de pura congelaci�n. Te cuento?
Strandhill es una playa donde el mar ruge muy bien, siempre est� lleno de surfistas en busca de buenas
olas. Y all� estaba yo tambi�n. Despu�s de unos meses viviendo en una ciudad sin costa, mis ganas por
hacer un poco de surfing estaban por las nubes. Aunque ten�a un �peque�o� problema: no ten�a equipo,
ni tabla, ni neopreno, y tampoco hab�a ninguna tienda para alquilarlo.
Todo se puso a rodar enseguida. Escrib� a un famoso surfista de la zona y recib� una respuesta
incre�ble. �Mi casa est� en la calle x, la puerta est� abierta y tienes la tabla en la esquina. Ven cuando
quieras�, me dijo. Y eso hice, fui para all� y la cog�. Aunque el neopreno no me lo pudo prestar, y no
porque se negara? Lamentablemente le sacaba unos 15 cm de altura. Luego, en la playa, un alem�n me
solucion� el tema del neopreno. Me prest� uno que hab�a por su maletero, uno muy fino, de los que uso
yo en el Mediterr�neo en oto�o o primavera. Y claro, era invierno y est�bamos en Irlanda.
El caso es que sal� del agua m�s pronto de lo previsto y con las manos, la cabeza y los labios
congelados. Me empec� a cambiar en el mismo paseo que contorneaba la costa y, estando
semidesnudo, se me acerc� Chris. �Est� fr�a el agua, eh�, apunt� este fen�meno.
Chris superaba los 65 a�os y todos los d�as hac�a un recorrido de decenas de kil�metros para llegar
hasta all�. Sus gracietas y su buena conversaci�n me hicieron apartar el fr�o de la parte de mi cabeza que
se encarga de pensar, y hasta cantamos juntos la canci�n de Annie.
S� que esto �ltimo puede sonar raro, �qui�n canta Annie semidesudo y congelado en un paseo de
Irlanda con un se�or que acaba de conocer? Pero? seguro que a ti tambi�n te han pasado cosas as�."


# EXPLICACI�N

Para la resoluci�n de esta tarea se han utilizado expresiones regulares. Un mecanismo que permite dectectar patrones en un string.

De esta manera, se ha abordado la resolucion del problema utilizando varias expresiones regulares como pueden ser la de identifiacion de caracteres y la identificacion de frases.

# C�DIGO

El problema se ha resuelto usando Python 3.7 y el IDE Visual Studio 2019.

La solucion se encuentra en el fichero "tarea_41.py" dentro de la carpeta "tarea_41" y consta de una region en la que se almacenan las funciones implementadas y el Main, el cual se ejecuta en cuanto se termina el codigo de la region anteriormente mencionada.

En cuanto a la forma de uso, simplemente hay que ejecutar el programa y visualizar los resultados obtenidos.

Cabe destacar que para que el programa funcione correctamente es necesario que el archivo de texto (Nombre.txt) se encuentre en la misma ruta que el archivo del proyecto (Tarea_41.py).

Nota: Dejo el enlace del programa en "Google Colab" para poder ejecutar el c�digo en linea. Para ello, se ha creado una variable tipo string que almacena el texto a analizar ya que no manejo la adicion de ficheros de texto en Google Colab.
(https://colab.research.google.com/drive/1SqaKpsGLV6IMCAdI4nouFJMojnyE8u-d?usp=sharing)


# POSIBLES MEJORAS
Como posibles mejoras se me ocurre calcular el porcentaje de aparicion de cada palabra en funcion del numero de palabras totales del texto.
Adem�s, a la hora de visualizar la lista ordenada, se podrian quitar los corchetes que encapsulan la clave-valor de cada elemento del diccionario.