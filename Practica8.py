import numpy as np
import cv2

cam = cv2.VideoCapture(1)

print('Presiona "espacio" para cerrar el video.')

while(cam.isOpened()):
    ready,hMirror = cam.read()
    imgOriginal = cv2.flip(hMirror,1)
