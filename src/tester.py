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
width = 1080
height = 1080

model = "models/model.obj"
size = V3(2.5, 2.5, 2.5)

#Se crea la instancia
rend = Renderer(width, height)

#rend.glClearColor(0,0.75,0)
#rend.glColor(1,1,1)
#rend.glClear()

rend.active_texture = Texture("models/model.bmp")

# Standard
#modelPos = V3(0, -250, -500)
#rend.glLookAt(V3(0, -250, -500), V3(0,0,0))
#rend.glLoadModel("models/statue.obj", modelPos, scale= V3(2.5, 2.5, 2.5), rotate=V3(-90,0,0))

rend.directional_light = V3(0, 0, -1)

# rend.active_shader = thermal
# modelPos = V3(0, 0, -10)
# rend.glLoadModel("models/model.obj", modelPos, scale= V3(4, 4, 4), rotate=V3(0,0,0))

# rend.active_shader = lines
# modelPos = V3(-4, 4, -10)
# rend.glLoadModel(model, modelPos, scale = size, rotate=V3(0,0,0))

# rend.active_shader = glow
# modelPos = V3(0, 4, -10)
# rend.glLoadModel(model, modelPos, scale = size, rotate=V3(0,0,0))

# rend.active_shader = negative
# modelPos = V3(4, 4, -10)
# rend.glLoadModel(model, modelPos, scale = size, rotate=V3(0,0,0))

# rend.active_shader = thermal
# modelPos = V3(-4, 0, -10)
# rend.glLoadModel(model, modelPos, scale = size, rotate=V3(0,0,0))

# rend.active_shader = zebra
# modelPos = V3(0, 0, -10)
# rend.glLoadModel(model, modelPos, scale = size, rotate=V3(0,0,0))

# rend.active_shader = static
# modelPos = V3(4, 0, -10)
# rend.glLoadModel(model, modelPos, scale = size, rotate=V3(0,0,0))

# rend.active_shader = points
# modelPos = V3(-4, -4, -10)
# rend.glLoadModel(model, modelPos, scale = size, rotate=V3(0,0,0))

# rend.active_shader = sky
# modelPos = V3(0, -4, -10)
# rend.glLoadModel(model, modelPos, scale = size, rotate=V3(0,0,0))

# rend.active_shader = triangleColor
# modelPos = V3(4, -4, -10)
# rend.glLoadModel(model, modelPos, scale = size, rotate=V3(0,0,0))

rend.active_shader = toon
modelPos = V3(-2.5, 2.5, -10)
rend.glLoadModel(model, modelPos, scale = size, rotate=V3(0,0,0))

rend.active_shader = lines
modelPos = V3(2.5, 2.5, -10)
rend.glLoadModel(model, modelPos, scale = size, rotate=V3(0,0,0))

rend.active_shader = sky
modelPos = V3(-2.5, -2.5, -10)
rend.glLoadModel(model, modelPos, scale = size, rotate=V3(0,0,0))

rend.active_shader = glow
modelPos = V3(2.5, -2.5, -10)
rend.glLoadModel(model, modelPos, scale = size, rotate=V3(0,0,0))

rend.glFinish("output.bmp")
