# Programa principal
from gl import Renderer, color
from msmath import V2, V3, sqroot, power, normalize, idMatrix, addMatrix, transposeMatrix, multMatrix, dotArray, scalarMultMatrix, detMatrix, invMatrix, tangent, sine, cosine, radians, degrees
from obj import Texture
from shaders import *
import random
from math import tan

#Se establece el ancho y la altura de la imagen
width = 1080
height = 1080

#Se crea la instancia
rend = Renderer(width, height)

rend.active_shader = lines

# rend.glClearColor(0,0,0)
#rend.glColor(0.4823,0.4823,0.4823)
#rend.glClear()
rend.active_texture = Texture("models/model.bmp")

# Standard
#modelPos = V3(0, -250, -500)
#rend.glLookAt(V3(0, -250, -500), V3(0,0,0))
#rend.glLoadModel("models/statue.obj", modelPos, scale= V3(2.5, 2.5, 2.5), rotate=V3(-90,0,0))

modelPos = V3(-4, 4, -10)
rend.glLoadModel("models/model.obj", modelPos, scale= V3(1.75, 1.75, 1.75), rotate=V3(0,0,0))

rend.active_shader = phong
modelPos = V3(0, 4, -10)
rend.glLoadModel("models/model.obj", modelPos, scale= V3(1.75, 1.75, 1.75), rotate=V3(0,0,0))

rend.active_shader = negative
modelPos = V3(4, 4, -10)
rend.glLoadModel("models/model.obj", modelPos, scale= V3(1.75, 1.75, 1.75), rotate=V3(0,0,0))

rend.active_shader = thermal
modelPos = V3(-4, 0, -10)
rend.glLoadModel("models/model.obj", modelPos, scale= V3(1.75, 1.75, 1.75), rotate=V3(0,0,0))

rend.active_shader = toon
modelPos = V3(0, 0, -10)
rend.glLoadModel("models/model.obj", modelPos, scale= V3(1.75, 1.75, 1.75), rotate=V3(0,0,0))

rend.active_shader = flat
modelPos = V3(4, 0, -10)
rend.glLoadModel("models/model.obj", modelPos, scale= V3(1.75, 1.75, 1.75), rotate=V3(0,0,0))

rend.active_shader = gouraud
modelPos = V3(-4, -4, -10)
rend.glLoadModel("models/model.obj", modelPos, scale= V3(1.75, 1.75, 1.75), rotate=V3(0,0,0))

rend.active_shader = unlit
modelPos = V3(0, -4, -10)
rend.glLoadModel("models/model.obj", modelPos, scale= V3(1.75, 1.75, 1.75), rotate=V3(0,0,0))

rend.active_shader = BWToon
modelPos = V3(4, -4, -10)
rend.glLoadModel("models/model.obj", modelPos, scale= V3(1.75, 1.75, 1.75), rotate=V3(0,0,0))

rend.glFinish("output.bmp")

