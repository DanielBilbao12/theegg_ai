# ENUNCIADO DE LA TAREA 22

Usted es un original empresario de Azkoitia, y tiene la brillante idea de abrir una tienda de la leche en la Plaza del pueblo. Como es una persona muy prudente, desea que la leche que venderá sea perfectamente natural y fresca, y por esa razón, va a traer unas sanísimas vacas de desde Tolosa. Dispone de un camión con un cierto límite de peso, y un grupo de vacas disponibles para la venta. Cada vaca puede tener un peso distinto, y producir una cantidad diferente de leche al día. Debes elegir qué vacas comprar y llevar en su camión, de modo que pueda maximizar la producción de leche, observando el límite de peso del camión.

1.- Para este propósito tienes que definir las siguientes entradas:

Entrada: Número total de vacas en la zona de Tolosa que están a la venta. 

Entrada: Peso total que el camión puede llevar. 

Entrada: Lista de pesos de las vacas. 

Entrada: Lista de la producción de leche por vaca, en litros por día.

2.- El algoritmo que programes tiene que calcular la siguiente salida:

Salida: Cantidad máxima de producción de leche se puede obtener.


# EXPLICACIÓN

Para la solucion de este ejercicio, se ha utilizado una funcion recursiva que calcula la produccion maxima de leche que se puede obtener teniendo en cuenta la tara del camion y las vacas disponibles.

En primer lugar, se ha creado una clase "Vaca" que almacena la masa, la produccion y un identificador numerico por cada una de las vacas que esten en venta.
Despues, se han creado unas funciones para verificar que los valores introducidos por el usuario son correctos. Estas funciones se utilizan en el main de manera que se asegura que las entradas son correctas.
En cuanto a la funcion recursiva, "CalculoDeProduccion", en primer lugar se evalua si hemos analizado todas las vacas disponibles, en caso de que no se hayan evaluado todos los casos, se almacena un objeto vaca de la lista de vacas disponibles a la variable "VacaPosible".
Entonces, si la tara del camion es menor a la que ya tenia mas el peso de la vaca posible ("VacaPosible"), esa vaca no puede ser cargada y se evalua el siguiente caso sin esta vaca.
En caso de que la tara del camion fuese mayor a la que tenia mas el peso de la vaca posible ("VacaPosible"), esa vaca puede ser cargada y se evalua el caso siguiente con esa vaca cargada y sin cargar, quedandonos con el caso en el que la produccion sea mayor.

De esta manera, se analizan todos los casos posibles y mediante la funcion max() se consigue el valor maximo de produccion que se puede obtener para cada uno de los casos


# CÓDIGO

El problema se ha resuelto usando Python 3.7 y el IDE Visual Studio 2019.

La solución se encuentra en la ruta theegg_ai/Tarea_22/Tarea_22, donde se pueden encontrar dos archivos con extension ".py". Entre estos, podemos destacar el archivo "vaca.py" que almacena la clase Vaca y el archivo "main.py" que almacena la solucion al problema.

En cuanto a la forma de uso, cuando se ejecuta el programa, este empieza preguntando la cantidad de vacas por tolosa, tara del camion y datos sobre las vacas. Cuando se determina la maxima produccion que se puede obtener, el programa pregunta si se desea hacer otro analisis con otras vacas y en caso de que se responda "NO" el programa se detiene y en caso de que se responda "SI" el programa se vuelve a ejecutar.

Nota: Dejo el enlace del programa en "Google Colab" para poder ejecutar el codigo en linea. Como no manejo el uso de modulos desde esa plataforma, creo la clase Vaca en el propio main para poder usarla. (https://colab.research.google.com/drive/1mksMCtJ7LdUpKsFBn-_KFkRSaig0D0kP?usp=sharing)


# REFERENCIAS

Cabe destacar, que para la resolucion de este ejercicio se han seguido varias referencias de interes:

	- Foro de TheEgg: Búsqueda heuristica en el algoritmo del lechero? 
		* Gracias a las sugerencias e ideas propuestas en este hilo del foro, me di cuenta de que la recursividad era una buena opcion para la resolucion de este ejercicio.
		* En particular, el README.md del repositorio de Eneko Bikandi (https://github.com/enekobi/theegg_ai) me ayudo mucho a entender la recursividad gracias a el arbol que tiene representado


	- Youtube: Video de la Universidad Catolica de Murcia (https://www.youtube.com/watch?v=XQYGwKiqV3Y)
		* En este video se representa el problema de las n-reinas (muy recomendable para entender el backtracking) y se analiza el problema con un arbol recursivo


# POSIBLES MEJORAS

Como posible mejora, se podria almacenar en una lista las vacas que se han comprado para obtener esa produccion maxima (podriamos almacenar los indices de las vacas) y a la hora de reflejar la cantidad maxima de produccion que se puede obtener, se podria reflejar con que vacas se obtendria ese valor. --> Mejora Aplicada