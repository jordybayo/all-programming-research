#coding:utf-8

from VideoCapture import Device
cam = Device()
#enregistrer le snapshot
cam.saveSnapshot('image.jpg')

#afficher les fenetres de reglage de la webcam
cam.displayCaptureFilterProprities()
cam.displayCapturePinProprities()