# Programa principal
from gl import Renderer, color
from msmath import V2, V3, sqroot, power, normalize, idMatrix, addMatrix, transposeMatrix, multMatrix, dotArray, scalarMultMatrix, detMatrix, invMatrix, tangent, sine, cosine, radians, degrees
from obj import Texture
import random
from math import tan

#Se establece el ancho y la altura de la imagen
width = 1080
height = 1080

# #Se crea la instancia
rend = Renderer(width, height)

rend.glClearColor(0,0,0)
rend.glColor(1,1,1)
rend.glClear()

#modelTex = Texture("models/model.bmp")

# Medium Shot
# modelPos = V3(75, -900, -300)
# rend.glLookAt(V3(0,0,-300), V3(0,0,0))
# rend.glLoadModel("models/statue.obj", None, modelPos, scale= V3(5, 5, 5), rotate=V3(-90,0,0))

# Low Angle
# modelPos = V3(75, -500, -500)
# rend.glLookAt(V3(75, 150, -500), V3(0,-150,0))
# rend.glLoadModel("models/statue.obj", None, modelPos, scale= V3(5, 5, 5), rotate=V3(-90,0,0))

# High Angle
# modelPos = V3(75, -600, -500)
# rend.glLookAt(V3(75, -200, -500), V3(0,0,0))
# rend.glLoadModel("models/statue.obj", None, modelPos, scale= V3(3, 3, 3), rotate=V3(-90,0,0))

# Dutch Angle
# modelPos = V3(-200, -200, -500)
# rend.glLookAt(V3(0, 0, -500), V3(0,0,0))
# rend.glLoadModel("models/statue.obj", None, modelPos, scale= V3(3, 3, 3), rotate=V3(-90,45,-45))

# Standard
modelPos = V3(0, -250, -500)
rend.glLookAt(V3(0, 0, -500), V3(0,0,0))
rend.glLoadModel("models/statue.obj", None, modelPos, scale= V3(2.5, 2.5, 2.5), rotate=V3(-90,0,0))

rend.glFinish("output.bmp")
