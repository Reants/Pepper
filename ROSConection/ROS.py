#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import qi
import rospy

session = qi.Session()
session.connect("tcp://192.168.0.102:9559")

speech = session.service("ALAnimatedSpeech")
photo = session.service("ALPhotoCapture")
memory_service = session.service("ALMemory")

def pituare():
    photo.setResolution(2)
    photo.setPictureFormat("jpg")
    photo.takePicture("/home/nao/TesisEmociones", "IC")
    
def connect_and_speak():
    rospy.init_node("Emotion_recognition")
    rospy.loginfo("Iniciando nodo de emociones")
    try:
        print("Conectado correctamente")
        speech.say(" C o n e x i n exitosa, ahora puedo hablar contigo.")
    except:
        print("Error al conectar con Pepper")
if __name__ == "__main__":
    connect_and_speak()