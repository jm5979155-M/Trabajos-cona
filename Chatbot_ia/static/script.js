async function enviarMensaje() {

    let mensaje = document.getElementById("mensaje").value.trim();

    if (mensaje === "") {
        return;
    }

    let chat = document.getElementById("chat");

    // Mostrar mensaje del usuario
    chat.innerHTML += `
        <p class="usuario">
            <strong>Tú:</strong> ${mensaje}
        </p>
    `;

    try {

        let respuesta = await fetch("/mensaje", {

            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({
                mensaje: mensaje
            })

        });

        let datos = await respuesta.json();

        // Mostrar respuesta del chatbot
        chat.innerHTML += `
            <p class="bot">
                <strong>Bot:</strong> ${datos.respuesta}
            </p>
        `;

    } catch (error) {

        chat.innerHTML += `
            <p class="bot">
                <strong>Bot:</strong> Ocurrió un error al procesar tu mensaje.
            </p>
        `;

        console.error(error);
    }

    // Limpiar caja de texto
    document.getElementById("mensaje").value = "";

    // Bajar automáticamente al último mensaje
    chat.scrollTop = chat.scrollHeight;
}

// Enviar mensaje al presionar Enter
document.getElementById("mensaje").addEventListener("keypress", function(event) {

    if (event.key === "Enter") {
        enviarMensaje();
    }

});