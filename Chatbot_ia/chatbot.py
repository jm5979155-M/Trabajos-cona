import json
import random
import re
import unicodedata
from datetime import datetime

with open('intents.json', encoding='utf-8') as archivo:
    datos = json.load(archivo)


# ELIMINA ACENTOS + SIGNOS + NORMALIZA TEXTO
def limpiar_texto(texto):

    texto = texto.lower()

    # quitar acentos
    texto = ''.join(
        c for c in unicodedata.normalize('NFD', texto)
        if unicodedata.category(c) != 'Mn'
    )

    # quitar signos especiales
    texto = re.sub(r'[¿?¡!.,;:]', '', texto)

    # espacios extra
    texto = texto.strip()

    return texto


def obtener_respuesta(mensaje_usuario):

    mensaje = limpiar_texto(mensaje_usuario)

    # PRESENTACIÓN
    if mensaje in ["quien eres", "como te llamas"]:
        return """Soy un chatbot desarrollado con Python y Flask.
Mi función es ayudarte a resolver dudas."""

    # SERVICIOS
    if mensaje == "que servicios ofrecen":
        return "Ofrecemos asesoría informática y desarrollo web."

    # UBICACIÓN (AHORA SÍ FUNCIONA)
    if mensaje in ["donde estan ubicados", "donde estan", "ubicacion"]:
        return "Nos encontramos en Tepic, Nayarit."

    # HORARIO
    if mensaje in ["cual es su horario", "a que hora abren"]:
        return "Nuestro horario es de lunes a viernes de 8:00 a.m. a 4:00 p.m."

    # TELÉFONO
    if mensaje in ["cual es su telefono", "telefono"]:
        return "Puedes comunicarte al 311-123-4567."

    # CONTACTO
    if mensaje in ["como puedo comunicarme"]:
        return """Puedes comunicarte al 311-123-4567.
También puedes escribirnos por correo electrónico."""

    # CORREO
    if mensaje in ["correo", "email", "correo electronico"]:
        return "Nuestro correo es contacto@empresa.com"

    # HORA
    if mensaje in ["que hora es", "que horas es"]:
        return f"La hora actual es {datetime.now().strftime('%H:%M:%S')}"

    # FECHA
    if mensaje in ["que dia es hoy", "dia actual"]:
        dias = [
            "Lunes","Martes","Miércoles",
            "Jueves","Viernes","Sábado","Domingo"
        ]
        return f"Hoy es {dias[datetime.now().weekday()]}"

    # TEMPERATURA
    if "temperatura" in mensaje:
        return "La temperatura aproximada en Tepic es de 30°C."

    # INTENTS JSON
    for intent in datos["intents"]:
        for patron in intent["patterns"]:
            if limpiar_texto(patron) in mensaje:
                return random.choice(intent["responses"])

    return "Lo siento, no entiendo tu pregunta."