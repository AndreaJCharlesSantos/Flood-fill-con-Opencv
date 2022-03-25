from multiprocessing.connection import wait
from typing import List
import cv2
import numpy as np
from skimage.filters import threshold_local

#Función que imprime la imagen
def display_img(img,nombre="Imagen"):
    cv2.imshow(nombre,img)
    cv2.waitKey()

#Lee el archivo de imagen y además cambia la dimensión
img = cv2.imread('unidad3.jpg')
img =cv2.resize(img,(800,800))
display_img(img, nombre = "Herramientas")

#Creamos una copia de la imagen (que es la que estará sujeta para el algoritmo)
imgC = img.copy()
# display_img(imgC, nombre = "Copia de herramientas")


# En esta parte hace la detección de los 'bordes' de la (o las) imágenes en el uso de este programa
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = cv2.GaussianBlur(gray, (5, 5), 0)
borde = cv2.Canny(gray, 75, 200)
display_img(borde, nombre = "Bordes")
cv2.waitKey()


#Usando esta librería hacer que se quite lo negro xd
warped1 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
T = threshold_local(warped1, 11, offset = 10, method = "gaussian")
warped1 = (warped1 > T).astype("uint8") * 255
cv2.imshow("originalImg", warped1)
cv2.waitKey()
