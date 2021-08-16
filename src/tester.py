# Programa principal
from gl import Renderer, color
from msmath import V2, V3, sqroot, power, normalize, idMatrix, addMatrix, transposeMatrix, multMatrix, dotArray, scalarMultMatrix, detMatrix, invMatrix, tangent, sine, cosine, radians, degrees
from obj import Texture
import random
from math import tan

#Se establece el ancho y la altura de la imagen
width = 1080
height = 1080

#Se crea la instancia
rend = Renderer(width, height)

rend.glClearColor(0,0,0)
rend.glColor(1,1,1)
rend.glClear()

modelTex = Texture("models/model.bmp")
modelPos = V3(0,0,-2)

rend.glLookAt(modelPos, V3(0,0,0))

rend.glLoadModel("models/model.obj", modelTex, modelPos, scale= V3(1, 1, 1), rotate=V3(0,45,0))

rend.glFinish("output.bmp")

matA = [
    [1, 2, 3],
    [-5, 7, 10],
    [3, -9, 4]
]
matB = [
    [4, 5, 2],
    [2, 8, 1],
    [-4, -5, -1]
]
matC = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
matD = [
    [1,2,3,4],
    [5,6,7,8]
]
matE = [
    [1, 3, -1],
    [-2, -1, 1]
]
matF = [
    [-4,  0,  3, -1],
    [ 5, -2, -1,  1],
    [-1,  2,  0,  6],
    [ 2, -3,  4,  7]
]
matG =[
    [1, 2],
    [3, 4]
]
matH = [
    [0, 0],
    [0, 0]
]
matI = [
    [3,6,3,4,1],
    [9,4,7,-8,3],
    [-5,0,9,-12,-5],
    [-1,-4,2,-10,11],
    [2,-7,5,14,-21]
]
matJ =[
    [3,0,2],
    [2,0,-2],
    [0,1,1]
]
matK = [
    [1],
    [3],
    [5],
    [7]
]

#print(multMatrix(matF, matK))
#print(invMatrix(matI))
