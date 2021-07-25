//let reconocimiento;

if (!("webkitSpeechRecognition" in window)) {
    alert("ERROR. NO PUEDE USAR LA API");
} else {
    reconocimiento = new webkitSpeechRecognition();
    reconocimiento.lang = "es-ES";
    reconocimiento.continuous = true;
    reconocimiento.interim = true;
    reconocimiento.addEventListener("result", iniciar);

}



function iniciar(event) {
    console.log("EMPIEZA EL RECONOCIMIENTO DE VOZ")
    for (i = event.resultIndex; i < event.results.length; i++) {
        document.getElementById("TextoReconocido").innerHTML = event.results[i][0].transcript;
    }
    //Funciones y variables de arrancar/detener videos

    //En primer lugar almaceno el reconocimiento en una variable y la printeo en consola para comprobar
    var texto = document.getElementById("TextoReconocido").innerText;
    console.log("EL TEXTO RECONOCIDO ES: " + texto);
    //Evaluo si coincide con la orden de PLAY
    if (texto = "iniciar") {
        document.getElementById("EtiquetaiFrame").autoplay();
    }

}

reconocimiento.start();
