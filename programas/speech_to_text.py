#instalar pyadio con el comando: pip install PyAudio
#instalar SpeechRecognition con el comando: pip install SpeechRecognition
import speech_recognition as sr

r = sr.Recognizer()

with sr.Microphone() as source:
    print('Escuchando...')
    audio = r.listen(source)
    
    try:
        text = r.recognize_google(audio, language="es-ES")
        print('Dijiste: {}'.format(text))
    except:
        print('No te he entendido')