import speech_recognition as sr

filename = "audio.wav"
output_file = "transcripcion_audio.txt"

r = sr.Recognizer()

# 1. Cargamos el archivo de audio
with sr.AudioFile(filename) as source:
    print("Leyendo el archivo...")
    audio_data = r.record(source) 

# 2. Intentamos la transcripción
try:
    print("Transcribiendo...")
    # Usamos el motor de Google en español
    text = r.recognize_google(audio_data, language="es-MX")
    
    # 3. Guardamos en el archivo .txt
    with open(output_file, "w") as f:
        f.write(text)
    
    print("Ya quedó, revisa el archivo transcripcion_audio.txt")
    print("Contenido:", text)

except Exception as e:
    print(f"Hubo un error: {e}")