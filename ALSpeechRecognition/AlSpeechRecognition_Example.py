"""Example: Use ALSpeechRecognition Module"""

import qi
import argparse
import sys
import time


def main(session):
    """
    This example uses the ALSpeechRecognition module.
    """
    # Get the service ALSpeechRecognition.

    asr_service = session.service("ALSpeechRecognition")

    asr_service.setLanguage("Spanish")

    # Example: Adds "yes", "no" and "please" to the vocabulary (without wordspotting)
    vocabulary = ["Feliz", "Contento", "Contenta", "Emocionado", "Emocionada", "Me", "Siento", "Muy", "Bien", "Alegría", "Eufórico", "Eufórica", "Estoy", "En", "Las", "Nubes", "Risueño", "Risueña", "Me", "Haces", "Feliz", "Entusiasmado", "Entusiasmada", "Estoy", "Lleno", "Llena", "De", "Energía", "Afortunado", "Afortunada", "Me", "Siento", "Bendecido", "Bendecida", "Radiante", "Optimista", "Satisfecho", "Satisfecha", "Extasiado", "Extasiada", "Pleno", "Plena", "Sonreír", "Vibrante", "Encantado", "Encantada", "Triunfante", "Animado", "Animada", "Celebrar", "Agradecido", "Agradecida", "Triste", "Estoy", "Triste", "Deprimido", "Deprimida", "No", "Me", "Siento", "Bien", "Llorar", "Necesito", "Un", "Abrazo", "Desilusionado", "Desilusionada", "Siento", "Un", "Vacío", "Desanimado", "Desanimada", "No", "Tengo", "Ganas", "De", "Nada", "Nostálgico", "Nostálgica", "Echo", "De", "Menos", "Aquellos", "Días", "Melancólico", "Melancólica", "Tengo", "El", "Corazón", "Roto", "Solitario", "Solitaria", "Abatido", "Abatida", "Angustiado", "Angustiada", "Desesperado", "Desesperada", "Cansado", "Cansada", "Frustrado", "Frustrada", "Herido", "Herida", "Afligido", "Afligida", "Desesperanzado", "Desesperanzada", "Descorazonado", "Descorazonada", "Vacío", "Vacía"]
    asr_service.setVocabulary(vocabulary, False)

    # Start the speech recognition engine with user Test_ASR
    asr_service.subscribe("Test_ASR")
    print 'Speech recognition engine started'
    time.sleep(20)
    asr_service.unsubscribe("Test_ASR")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", type=str, default="127.0.0.1",
                        help="Robot IP address. On robot or Local Naoqi: use '127.0.0.1'.")
    parser.add_argument("--port", type=int, default=9559,
                        help="Naoqi port number")

    args = parser.parse_args()
    session = qi.Session()
    try:
        session.connect("tcp://" + args.ip + ":" + str(args.port))
    except RuntimeError:
        print ("Can't connect to Naoqi at ip \"" + args.ip + "\" on port " + str(args.port) +".\n"
               "Please check your script arguments. Run with -h option for help.")
        sys.exit(1)
    main(session)