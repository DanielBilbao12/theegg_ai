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
}

//Funciones para el control de los videos
function ArrancarVideo() {
    var Video = document.getElementById("EtiquetaVideo");
    var Youtube = document.getElementById("EtiquetaiFrame");
    Video.pause();
    Youtube.pause();
    while (texto != "iniciar") {
        Video.pause();
        Youtube.pause();
    }
    Video.play();
    Youtube.play();
}

function PararVideo() {
    var Video = document.getElementById("EtiquetaVideo");
    var Youtube = document.getElementById("EtiquetaiFrame");
    if (texto = "detener") {
        Video.pause();
        Youtube.pause();
    }
}

reconocimiento.start();