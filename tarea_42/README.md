# ENUNCIADO DE LA TAREA 42
El alumno para superar la tarea debe:

- Diseñar una estructura básica de HTML y verla en el navegador.

- Introducir algo de color a la página apoyandose en CSS.

- Añadir un video gracias a la etiqueta video de HTML5.

- Opcional: Darle al play y al pause al video mediante intrucciones por voz utilizando javascript.

# EXPLICACIÓN

Para la resolución del ejercicio, en primer lugar se ha aprendido a programar documentos en HTML5:

- Se ha creado una pagina principal, una de pruebas y una de enlaces.

- La pagina principal contiene un breve resumen sobre la escuela y el enunciado de la tarea a realizar.

- La página de pruebas contiene diferentes secciones en las que se han realizado las pruebas a la hora de aprender a programar este tipo de documentos web.

- La pagina de enlaces contiene dos videos: Un video insertado con la etiqueta "video" (este es el video que se controla por voz) y otro video insertado mediante la etiqueta "iframe".

- En todas las paginas hay una zona con las paginas mencionadas vinculadas para poder navegar entre ellas.

Una vez definido el contenido de cada una de las paginas web, se ha aprendido a agregar estilos a las mismas mediante CSS:

- Se han creado tres hojas de estilo, una por cada página.

Por último, se les ha agregado "dinamica" a la página de pruebas y a la de enlaces:

- En la página de pruebas, al rellenar el formulario y enviarlo pulsando el boton, se muestran los datos introducidos por consola.

- En la página de enlaces, se permite controlar la reproducion del video insertado mediante la etiqueta "video" por voz. Para ello, se ha utilizadola API Web Speech de JavaScript: [Enlace](https://wicg.github.io/speech-api/) 
	
	- Se deben aceptar los permisos del microfono al navegador

	- Se debe activar el video manualmente la primera vez pulsando el boton "PLAY/PAUSE"

	- Diciendo "reproducir" se arranca el video, "detener" pausa el video y "reiniciar" reinicia el video.

# CÓDIGO

El problema se ha resuelto usando HTML5, CSS y JavaScript mediante el IDE Visual Studio 2019.

La solución se encuentra en la misma ruta que el archivo que esta leyendo (README.md), es decir, dentro del repositorio de The Egg, en la carpeta "tarea_42".

En cuanto a la forma de uso, simplemente hay que descargar la carpeta anteriormente mencionada con todos sus archivos ("tarea_42") y abrir el archivo "index.html" con un navegador (RECOMENDABLE GOOGLE CHROME). 

Para clonar una única carpeta del repositorio (evitando tener que clonaros todo mi repositorio): [Seguir este enlace](https://www.montesinos.org.es/2018/04/welcome-file.html) 

# REFERENCIAS

Cabe destacar, que para la resolucion de este ejercicio se han seguido varias referencias de interes:

	- Tutorial completo de HTML: https://www.w3schools.com/html/default.asp
	- Curso HTML para principiantes: https://www.youtube.com/watch?v=rbuYtrNUxg4
	- Tutorial HTML5: APIs en HTML5: https://www.youtube.com/watch?v=91CxoB6DHHY
	- Web de Arkaitz Garro con un extenso resumen de HTML5: https://www.arkaitzgarro.com/html5/
	- Emoticonos para insertar en HTML5: http://www.iemoji.com/#?category=symbols&version=36&theme=appl&skintone=default
	- Video resumen: https://www.youtube.com/watch?v=mNbnV3aN3KA
	- Explicacion sobre la sintaxis de CSS: https://www.quackit.com/css/tutorial/css_syntax.cfm
	- Guia sobre agregar estilos a listas en CSS: https://guidacode.com/2016/css/modificando-listas-css/
	- Video explicativo sobre como agregar reconocimiento de voz a una web con JavaScript: https://www.youtube.com/watch?v=2cXB8yyz8gc