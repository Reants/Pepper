import qi
import time
import argparse
import sys

#Concetar a Pepper
session = qi.Session()
session.connect("tcp://127.0.0.1:9559")

asr_service = session.service("ALSpeechRecognition")
asr_memory = session.service("ALMemory")
asr_service.setLanguage("Spanish")

# Example: Adds "yes", "no" and "please" to the vocabulary (without wordspottin$
vocabulary = ["Feliz", "Contento", "Contenta", "Emocionado", "Emocionada", "Me", "Siento", "Muy", "Bien", "Alegria", "Euforico", "Euforica", "Estoy", "En", "Las", "Nubes", "Risueno", "Risuena", "Me", "Haces", "Feliz", "Entusiasmado", "Entusiasmada", "Estoy", "Lleno", "Llena", "De", "Energia", "Afortunado", "Afortunada", "Me", "Siento", "Bendecido", "Bendecida", "Radiante", "Optimista", "Satisfecho", "Satisfecha", "Extasiado", "Extasiada", "Pleno", "Plena", "Sonreir", "Vibrante", "Encantado", "Encantada", "Triunfante", "Animado", "Animada", "Celebrar", "Agradecido", "Agradecida", "Triste", "Estoy", "Triste", "Deprimido", "Deprimida", "No", "Me", "Siento", "Bien", "Llorar", "Necesito", "Un", "Abrazo", "Desilusionado", "Desilusionada", "Siento", "Un", "Vacio", "Desanimado", "Desanimada", "No", "Tengo", "Ganas", "De", "Nada", "Nostalgico", "Nostalgica", "Echo", "De", "Menos", "Aquellos", "Dias", "Melancolico", "Melancolica", "Tengo", "El", "Corazon", "Roto", "Solitario", "Solitaria", "Abatido", "Abatida", "Angustiado", "Angustiada", "Desesperado", "Desesperada", "Cansado", "Cansada", "Frustrado", "Frustrada", "Herido", "Herida", "Afligido", "Afligida", "Desesperanzado", "Desesperanzada", "Descorazonado", "Descorazonada", "Vacio", "Vacia"]
# Pausar el motor ASR para realizar cambios
asr_service.pause(True)
asr_service.setVocabulary(vocabulary, False)
asr_service.pause(False)

# Start the speech recognition engine with user Test_ASR
asr_service.subscribe("Test_ASR")
print('Speech recognition engine started')
time.sleep(20)

def word_recognized_callback(value):
        print('Estoy aqui')
        if value and isinstance(value, list):
                recognized_word = value[0]  # La palabra reconocida
                confidence = value[1]        # La confianza del reconocimiento
                print("Palabra reconocida: {recognized_word} con confianza: {confidence}")

# Conectar el evento WordRecognized a la funcion de callback
print("Palabra reconocida: {recognized_word} con confianza: {confidence}")


try:
        while True:
                time.sleep(1)
finally:
        asr_service.unsubscribe("Test_ASR")
