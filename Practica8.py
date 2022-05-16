import numpy as np
import cv2

cam = cv2.VideoCapture(1)

print('Presiona "espacio" para cerrar el video.')

while(cam.isOpened()):
    ready,hMirror = cam.read()
    imgOriginal = cv2.flip(hMirror,1)
    
    laplacian = cv2.Laplacian(imgOriginal, cv2.CV_64F)
    Sobelx = cv2.Sobel(imgOriginal, cv2.CV_64F,1,0,ksize=5)
    Sobely = cv2.Sobel(imgOriginal, cv2.CV_64F,0,1,ksize=5)
    Sobel = cv2.Sobel(imgOriginal, cv2.CV_64F,1,1,ksize=5)
    edges = cv2.Canny(imgOriginal, 100, 100)
    
    if ready == True:
        cv2.imshow('Original',imgOriginal)
        cv2.imshow('Laplacian',laplacian)
        cv2.imshow('Sobel X',Sobelx)
        cv2.imshow('Sobel Y',Sobely)
        cv2.imshow('Sobel',Sobel)
        cv2.imshow('Edges',edges)
        if cv2.waitKey(1) & 0xFF == ord(' '):
            cv2.destroyAllWindows()
            break

