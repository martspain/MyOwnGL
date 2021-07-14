# Programa principal
from gl import Renderer, V2, color

#Se establece el ancho y la altura de la imagen
width = 960
height = 540

#Se crea la instancia
rend = Renderer(width, height)

#Se crea el viewport de modo que ocupe toda la ventana
rend.glViewport(0,0,width,height)

#Se establece el color de fondo dorado
rend.glClearColor(0.9, 0.8, 0)

#Se hace reset de la ventana
rend.glClear()

#Se le asigna color de escritura a morado
rend.glColor(0.4, 0, 0.6)

#Se crea un punto en el viewport, en la coordenada normalizada (0,0) es decir, en el centro del viewport
#rend.glVertex(0,0)

#Se crea una linea que atraviese todo el viewport
rend.glLine(V2(0,0), V2(width, height))
#Se crea otra linea que atraviese todo el viewport para formar una X
rend.glLine(V2(0, height), V2(width, 0))

#Se crea la funcion x^2
# for x in range(width):
#     x0 = x
#     x1 = x + 1
#     y0 = (x0 * x0 * x0)
#     y1 = (x1 * x1 * x1)

#     rend.glLine(V2(int(x0), int(y0)), V2(int(x1), int(y1)))

rend.glFinish("output.bmp")