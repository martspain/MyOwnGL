# Programa principal
from gl import Renderer, color
from msmath import V2, V3, sqroot, power, normalize, identityMatrix
from obj import Texture
import random

#Se establece el ancho y la altura de la imagen
width = 1080
height = 1080

#Se crea la instancia
rend = Renderer(width, height)

rend.glClearColor(0,0,0)
rend.glColor(1,1,1)
rend.glClear()

modelTex = Texture("models/model.bmp")

rend.glLoadModel("models/model.obj", modelTex, V3(int(width/2), int(height/2), 0), V3(450, 450, 450))

rend.glFinish("output.bmp")