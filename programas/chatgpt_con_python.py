#Para utilizar, instalar OPENAI con el comando: pip install openai==0.28
#Instalar pyttsx3 con el comando: pip install pyttsx3
#Instalar Keyboard con el comando: pip install keyboard
import openai
import pyttsx3
import speech_recognition as sr
import keyboard
import threading

# Configura tu clave de API de OpenAI
openai.api_key = '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'

reproduciendo = False
detener_reproduccion = False

def chatgpt(pregunta):
      global reproduciendo
      global detener_reproduccion
      
      respuesta = openai.Completion.create(engine='text-davinci-003',prompt=pregunta ,max_tokens=2048)      
      respuesta = respuesta.choices[0].text
      print(respuesta)
      
      reproducir_texto(respuesta)

      
def reproducir_texto(respuesta):

      if respuesta == 'hasta pronto':
            print('hasta pronto')
            
      engine = pyttsx3.init()
      engine.setProperty('rate', 180)
      engine.say(respuesta)
      engine.runAndWait()
      

def menu():
      
      despedida = "hasta pronto"
      
      while True:
                       
            opcion = input('\nPreguntar por: 1)Texto 2)Voz: ')
            
            if opcion == '1':
                  pregunta = input("\nQue desea preguntar?: ")
                  
                  if pregunta == 'exit' or pregunta == 'salir':
                        reproducir_texto(despedida)
                        break
                  
                  chatgpt(pregunta)

            elif opcion == '2':
                  r = sr.Recognizer()

                  with sr.Microphone() as source:
                        print('\nEscuchando...')
                        audio = r.listen(source)
                        
                        try:
                              text = r.recognize_google(audio, language="es-ES")
                              print('\nDijiste: {}'.format(text))
                              chatgpt(text)
                        except:
                              print('No te he entendido')
            
            elif opcion == 'salir' or opcion == 'exit':
                  reproducir_texto(despedida)
                  break
            
            else:
                  print('Opcion incorrecta')
                  menu()

menu()

      
      
      
