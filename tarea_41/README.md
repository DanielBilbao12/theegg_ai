# ENUNCIADO DE LA TAREA 41

Para esta tarea se propone que el alumno mediante tecnicas Regex calcule el numero de caracteres, el numero de palabras y el ranking de palabras por frecuencia de uso del siguiente texto:

"En Strandhill, Irlanda, se cruzó en mi camino Chris, un señor de los que inspiran y se posicionan como
referente. Fue una pieza fundamental en un momento de pura congelación. Te cuento?
Strandhill es una playa donde el mar ruge muy bien, siempre está lleno de surfistas en busca de buenas
olas. Y allí estaba yo también. Después de unos meses viviendo en una ciudad sin costa, mis ganas por
hacer un poco de surfing estaban por las nubes. Aunque tenía un «pequeño» problema: no tenía equipo,
ni tabla, ni neopreno, y tampoco había ninguna tienda para alquilarlo.
Todo se puso a rodar enseguida. Escribí a un famoso surfista de la zona y recibí una respuesta
increíble. «Mi casa está en la calle x, la puerta está abierta y tienes la tabla en la esquina. Ven cuando
quieras», me dijo. Y eso hice, fui para allá y la cogí. Aunque el neopreno no me lo pudo prestar, y no
porque se negara? Lamentablemente le sacaba unos 15 cm de altura. Luego, en la playa, un alemán me
solucionó el tema del neopreno. Me prestó uno que había por su maletero, uno muy fino, de los que uso
yo en el Mediterráneo en otoño o primavera. Y claro, era invierno y estábamos en Irlanda.
El caso es que salí del agua más pronto de lo previsto y con las manos, la cabeza y los labios
congelados. Me empecé a cambiar en el mismo paseo que contorneaba la costa y, estando
semidesnudo, se me acercó Chris. «Está fría el agua, eh», apuntó este fenómeno.
Chris superaba los 65 años y todos los días hacía un recorrido de decenas de kilómetros para llegar
hasta allí. Sus gracietas y su buena conversación me hicieron apartar el frío de la parte de mi cabeza que
se encarga de pensar, y hasta cantamos juntos la canción de Annie.
Sé que esto último puede sonar raro, ¿quién canta Annie semidesudo y congelado en un paseo de
Irlanda con un señor que acaba de conocer? Pero? seguro que a ti también te han pasado cosas así."


# EXPLICACIÓN

Para la resolución de esta tarea se han utilizado expresiones regulares. Un mecanismo que permite dectectar patrones en un string.

De esta manera, se ha abordado la resolucion del problema utilizando varias expresiones regulares como pueden ser la de identifiacion de caracteres y la identificacion de frases.

# CÓDIGO

El problema se ha resuelto usando Python 3.7 y el IDE Visual Studio 2019.

La solucion se encuentra en el fichero "tarea_41.py" dentro de la carpeta "tarea_41" y consta de una region en la que se almacenan las funciones implementadas y el Main, el cual se ejecuta en cuanto se termina el codigo de la region anteriormente mencionada.

En cuanto a la forma de uso, simplemente hay que ejecutar el programa y visualizar los resultados obtenidos.

Cabe destacar que para que el programa funcione correctamente es necesario que el archivo de texto (Nombre.txt) se encuentre en la misma ruta que el archivo del proyecto (Tarea_41.py).

Nota: Dejo el enlace del programa en "Google Colab" para poder ejecutar el código en linea. Para ello, se ha creado una variable tipo string que almacena el texto a analizar ya que no manejo la adicion de ficheros de texto en Google Colab.
(https://colab.research.google.com/drive/1SqaKpsGLV6IMCAdI4nouFJMojnyE8u-d?usp=sharing)


# POSIBLES MEJORAS
Como posibles mejoras se me ocurre calcular el porcentaje de aparicion de cada palabra en funcion del numero de palabras totales del texto.
Además, a la hora de visualizar la lista ordenada, se podrian quitar los corchetes que encapsulan la clave-valor de cada elemento del diccionario.