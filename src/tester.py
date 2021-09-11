# Programa principal
from gl import Renderer, color
from msmath import *
from obj import Texture
from shaders import *
import random
from math import tan
import time
import datetime
import timeit

#Se establece el ancho y la altura de la imagen
width = 1920
height = 1080

#Se crea la instancia
rend = Renderer(width, height)

#rend.glClearColor(0,0.75,0)
#rend.glColor(1,1,1)
#rend.glClear()

rend.directional_light = V3(0, 0, -1)

rend.background = Texture("models/park.jpg")
rend.glClearBackground()

model = "models/tree.obj"
size = V3(0.1, 0.1, 0.1)
modelPos = V3(17, -7, -25)
rend.active_shader = zebra
rend.glLoadModel(model, modelPos, scale = size, rotate=V3(0,0,0))

model = "models/squirrel.obj"
size = V3(0.4, 0.4, 0.4)
modelPos = V3(-10, -4, -12)
rend.active_shader = thermal
rend.glLoadModel(model, modelPos, scale = size, rotate=V3(0,60,0))

model = "models/statue.obj"
size = V3(0.1, 0.1, 0.1)
modelPos = V3(0, -17, -70)
rend.active_texture = Texture("models/blackMarble.jpg")
rend.active_shader = glow
rend.glLoadModel(model, modelPos, scale = size, rotate=V3(-90,0,0))

model = "models/sonic.obj"
size = V3(0.5, 0.5, 0.5)
modelPos = V3(27, -20, -90)
rend.active_shader = triangleColor
rend.glLoadModel(model, modelPos, scale = size, rotate=V3(0,40,0))

model = "models/snail.obj"
rend.active_texture = Texture("models/bench.png")
size = V3(0.3, 0.3, 0.3)
modelPos = V3(0, -4, -10)
rend.active_shader = sky
rend.glLoadModel(model, modelPos, scale = size, rotate=V3(0,135,0))

rend.glFinish("output.bmp")
