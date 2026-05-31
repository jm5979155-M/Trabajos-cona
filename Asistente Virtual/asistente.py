import pygame
import speech_recognition as sr
import subprocess
import os
import sys

def reconocer_audio(ruta_audio):
    """Reconoce el contenido del archivo de audio .wav"""
    recognizer = sr.Recognizer()
    
    try:
        with sr.AudioFile(ruta_audio) as source:
            print(f"Procesando audio: {ruta_audio}")
            audio = recognizer.record(source)
            
        try:
            texto = recognizer.recognize_google(audio, language='es-ES')
            print(f"Texto reconocido: {texto}")
            return texto.lower()
        except sr.UnknownValueError:
            print("No se pudo entender el audio")
            return None
        except sr.RequestError as e:
            print(f"Error al conectar con el servicio de reconocimiento: {e}")
            return None
            
    except Exception as e:
        print(f"Error al cargar el archivo de audio: {e}")
        return None

def ejecutar_instruccion(texto):
    """Ejecuta la instrucción según el texto reconocido"""
    
    if texto is None:
        print("No se pudo procesar la instrucción")
        return
    
    # Instrucciones disponibles
    if "abrir youtube" in texto or "abrir el reproductor de vídeo" in texto:
        print("▶️ Abriendo YouTube/Reproductor de vídeo...")
        try:
            # Para Windows - abre YouTube en navegador predeterminado
            subprocess.run(["start", "https://www.youtube.com"], shell=True)
            print("✅ YouTube abierto correctamente")
        except Exception as e:
            print(f"❌ Error: {e}")
            
    elif "abrir word" in texto:
        print("📝 Abriendo Microsoft Word...")
        try:
            # Para Windows
            subprocess.run(["start", "winword"], shell=True)
            print("✅ Word abierto correctamente")
        except Exception as e:
            print(f"❌ Error: {e}")
            
    elif "apagar el equipo" in texto or "apagar el sistema" in texto:
        print("⚠️ Preparando para apagar el sistema...")
        respuesta = input("¿Estás seguro de que quieres apagar el equipo? (s/n): ")
        if respuesta.lower() == 's':
            print("🔄 Apagando el sistema...")
            try:
                # Para Windows
                subprocess.run(["shutdown", "/s", "/t", "10"], shell=True)
                print("✅ El equipo se apagará en 10 segundos")
                print("Para cancelar: shutdown /a")
            except Exception as e:
                print(f"❌ Error: {e}")
        else:
            print("❌ Apagado cancelado")
    else:
        print(f"❌ Instrucción no reconocida: '{texto}'")
        print("Instrucciones disponibles:")
        print("  - ABRIR EL REPRODUCTOR DE VÍDEO")
        print("  - ABRIR WORD")
        print("  - APAGAR EL EQUIPO")

def mostrar_menu():
    """Muestra el menú de selección de audios"""
    audios = {
        "1": ("abrir_youtube.wav", "Abrir YouTube"),
        "2": ("abrir_word.wav", "Abrir Word"),
        "3": ("apagar_el_sistema.wav", "Apagar el equipo")
    }
    
    print("\n" + "="*50)
    print("🎤 SELECCIONA EL AUDIO A PROCESAR")
    print("="*50)
    print("1. abrir_youtube.wav (Abrir YouTube)")
    print("2. abrir_word.wav (Abrir Word)")
    print("3. apagar_el_sistema.wav (Apagar el equipo)")
    print("0. Salir")
    print("="*50)
    
    while True:
        opcion = input("\n👉 Elige una opción (1, 2, 3 o 0): ").strip()
        
        if opcion == "0":
            print("👋 Saliendo del programa...")
            return None, None
        elif opcion in audios:
            nombre_audio, descripcion = audios[opcion]
            return nombre_audio, descripcion
        else:
            print("❌ Opción no válida. Intenta de nuevo.")

def main():
    # Inicializar pygame para manejar audio
    pygame.mixer.init()
    
    print("🎤 SISTEMA DE RECONOCIMIENTO DE VOZ")
    print("Este programa procesa archivos .wav y ejecuta comandos")
    
    while True:
        # Mostrar menú y obtener selección
        nombre_audio, descripcion = mostrar_menu()
        
        if nombre_audio is None:  # Salir del programa
            break
        
        # Verificar si el archivo existe
        if not os.path.exists(nombre_audio):
            print(f"\n❌ ERROR: No se encontró el archivo '{nombre_audio}'")
            print(f"Asegúrate de que el archivo esté en la misma carpeta que el programa")
            input("\nPresiona Enter para continuar...")
            continue
        
        print(f"\n🎵 Procesando: {descripcion}")
        print("⏳ Reconociendo instrucción...")
        
        # Reconocer el audio
        texto_instruccion = reconocer_audio(nombre_audio)
        
        if texto_instruccion:
            print(f"\n📝 Instrucción detectada: '{texto_instruccion}'")
            print("\n🚀 Ejecutando comando...")
            ejecutar_instruccion(texto_instruccion)
        else:
            print("\n❌ No se pudo reconocer la instrucción del audio")
        
        print("\n" + "-"*50)
        input("Presiona Enter para continuar...")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n👋 Programa interrumpido por el usuario")
        sys.exit(0)
    except Exception as e:
        print(f"\n❌ Error inesperado: {e}")
        input("Presiona Enter para salir...")