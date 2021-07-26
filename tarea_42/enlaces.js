//Botones control de video
var Video = document.getElementById("EtiquetaVideo");
alert("EN PRIMER LUGAR, HACE FALTA INICIAR EL VIDEO MANUALMENTE PARA POSTERIORMENTE CONTROLARLO POR VOZ, ADEMAS DEBE PERMITIR EL USO DEL MICROFONO");
function PausaPlay() {
    if (Video.paused)
        Video.play();
    else
        Video.pause();
}
function Restart() {
    Video.pause();
    Video.currentTime = 0;
}
//Reconocimiento de voz
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
    //En primer lugar almaceno el reconocimiento en una variable y la printeo en consola para comprobar
    var texto = document.getElementById("TextoReconocido").innerText;
    console.log("EL TEXTO RECONOCIDO ES: " + texto);
    //Evaluo si coincide con las ordenes--> ANTES DE CONTROLAR EL VIDEO POR VOZ, HACE FALTA INICIARLO UNA VEZ MANUALMENTE
    if (texto == "reproducir")
        Video.play();
    if (texto == "detener")
        Video.pause();
    if (texto == "reiniciar")
        Restart();

}

reconocimiento.start();
