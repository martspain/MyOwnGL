# Programa principal
from gl import Renderer, V2, color
import random

#Se establece el ancho y la altura de la imagen
width = 720
height = 1080

#Se crea la instancia
rend = Renderer(width, height)

rend.glClearColor(0,0,0)
rend.glColor(1,1,1)
rend.glClear()

rend.glLoadModel("statue.obj", V2(width/2, 0), V2(5.3, 5.3))
# Diseño alterno
#rend.glLoadModel("statue.obj", V2(1.5 * width/5, 0), V2(5.3, 5.3))
#rend.glLoadModel("statue.obj", V2(3.5 * width/5, 0), V2(5.3, 5.3), True)

rend.glFinish("output.bmp")