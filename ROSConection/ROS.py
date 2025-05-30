#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#This is with ROS noetic

import qi
import rospy

session = qi.Session()
ip = 192.168.0.102
session.connect("tcp://" + ip +":9559")

speech = session.service("ALAnimatedSpeech")
photo = session.service("ALPhotoCapture")
memory_service = session.service("ALMemory")
    
def connect_and_speak():
    rospy.init_node("Emotion_recognition")
    rospy.loginfo("Iniciando nodo de emociones")
    try:
        print("Conectado correctamente")
        speech.say(" Conexion exitosa, ahora puedo hablar contigo.")
    except:
        print("Error al conectar con Pepper")
if __name__ == "__main__":
    connect_and_speak()
