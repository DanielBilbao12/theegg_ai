let reconocimiento;

if (!("webkitSpeechRecognition" in window)) {
    alert("ERROR. NO PUEDE USAR LA API");
} else {
    reconocimiento = new webkitSpeechRecognition();
    reconocimiento.lang = "es-ES";
    reconocimiento.continuous = true;
    reconocimiento.interim = true;
    reconocimiento.addEventListener("resultado", iniciar);

}

function iniciar(event) {
    for (i = event.resultIndex; i < event.results.length; i++) {
        console.log(""+event.results[i][0].transcript);
    }
}

reconocimiento.start();