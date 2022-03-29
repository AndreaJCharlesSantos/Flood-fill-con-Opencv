import cv2
import numpy as np


class Node:
    def __init__(self, x, y, label):
        self.x = x
        self.y = y
        self.label = label

def display_img(img,nombre="Imagen"):
    cv2.imshow(nombre,img)
    cv2.waitKey()

def main():

    img = cv2.imread('unidad3.jpg',0)
    img = cv2.resize(img, (500, 500))
    display_img(img, nombre = "Imagen original")
    copia = img.copy()
    #Binarización de la imagen
    ncopy = cv2.threshold(copia,128,255,  cv2.THRESH_BINARY_INV)[1]
    # Cambiando el fondo a negro y lo demás a blanco
    display_img(ncopy, nombre = "Copia de imagen")
    cv2.waitKey()
    regiones = regionLabeling(ncopy)
    display_img(regiones, nombre = "Regiones")
    cv2.waitKey()
    pass

def regionLabeling(img):
    n = 1
    height, width = img.shape
    for u in range(height):
        for v in range(width):
            if img[u][v] == 255:
                flood_fill_depth_first(img, u, v, n)
                n += 1
    return colorRegion(img)

def colorRegion(img):
    height, width = img.shape
    img_color = np.zeros((height, width, 3), np.uint8)
    colors = {}
    for key in set(img.flatten()):
        if key != 0:
            colors[key] = np.random.randint(0, 256, 3)

    for u in range(height):
        for v in range(width):
            if img[u][v] != 0:
                img_color[u,v] = colors[img[u,v]]   
    return img_color
    

def flood_fill_depth_first(img, u, v, label):
    stack = []
    stack.append(Node(u, v, label))
    while not (len(stack) == 0):
        node = stack.pop()
        x = node.x
        y = node.y
        label = node.label
        if img[y][x] == 255:
            img[y][x] = label
            if x < img.shape[1] - 1:
                stack.append(Node(x + 1, y, label))
            if x > 0:
                stack.append(Node(x - 1, y, label))
            if y < img.shape[0] - 1:
                stack.append(Node(x, y + 1, label))
            if y > 0:
                stack.append(Node(x, y - 1, label))



if __name__ == "__main__":
    main()
