# Programa principal
from gl import Renderer, V2, color
import random

#Se establece el ancho y la altura de la imagen
width = 1920
height = 1080

#Se crea la instancia
rend = Renderer(width, height)

#Se crea el viewport de modo que ocupe toda la ventana
#rend.glViewport(0,0,width,height)

#Se establece el color de fondo dorado
#rend.glClearColor(0.9, 0.8, 0)
rend.glClearColor(0, 0, 0)

#Se hace reset de la ventana
rend.glClear()

#Se le asigna color de escritura a morado
#rend.glColor(0.4, 0, 0.6)
#rend.glColor(1, 0, 1)
rend.glColor(1,0,0)

#Se crea un punto en el viewport, en la coordenada normalizada (0,0) es decir, en el centro del viewport
#rend.glVertex(0,0)

#Se crea una linea que atraviese todo el viewport
#rend.glLine(V2(0,0), V2(int(width/80), int(height/80)))
#Se crea otra linea que atraviese todo el viewport para formar una X
#rend.glLine(V2(0, height), V2(width, 0))

#Se crea la funcion x^2
# for x in range(width):
#     x0 = x
#     x1 = x + 1
#     y0 = (x0 * x0 * x0)
#     y1 = (x1 * x1 * x1)

#     rend.glLine(V2(int(x0), int(y0)), V2(int(x1), int(y1)))

# Experimento 2 (queria hacer cada pixel de diferente color pero termino siendo un degradado o estatica)

pixelCount = width * height
counter = 0
locx = 0
locy = 0

while counter < pixelCount:
    while locx < width:
        while locy < height:
            #Degradado de un color
            #rend.glPoint(locx, locy, color(counter/(2 * pixelCount), counter/(3 * pixelCount), counter/(1 * pixelCount)))
            
            #Estatica
            #rend.glPoint(locx, locy, color(random.random(), random.random(), random.random()))
            
            #Degradado de varios colores
            #rend.glPoint(locx, locy, color(locy/height, locx/width, locy/height))
            rend.glPoint(locx, locy, color(locx/width, locx/width, locy/height))
            #rend.glPoint(locx, locy, color(locy/height, locx/width, locx/width))
            
            locy += 1
            counter += 1
            #print("Y count: " + str(locy))
        locx += 1
        locy = 0
        counter += 1
        #print("X count: " + str(locx))

#Experimento 1 Curvas con lineas rectas

intensity = 150
for x in range(intensity):
    rend.glLine(V2(int(x * width/intensity),0), V2(width, int(x * height/intensity)))
for x in range(intensity):
    rend.glLine(V2(width, int(x * height/intensity)), V2(int(width - x * width/intensity), height))
for x in range(intensity):
    rend.glLine(V2(int(x * width/intensity),0), V2(0, int(height - x * height/intensity)))
for x in range(intensity):
    rend.glLine(V2(0, int(x * height/intensity)), V2(int(x * width/intensity), height))

# Cruz de curvas con lineas rectas
# for x in range(intensity):
#     rend.glLine(V2(int(x * width/(2*intensity)), int(height/2)), V2(int(width/2), int(height/2 + x * height/(2*intensity))))
# for x in range(intensity):
#     rend.glLine(V2(int(width - x * width/(2*intensity)), int(height/2)), V2(int(width/2), int(height/2 + x * height/(2*intensity))))
# for x in range(intensity):
#     rend.glLine(V2(int(x * width/(2*intensity)), int(height/2)), V2(int(width/2), int(height/2 - x * height/(2*intensity))))
# for x in range(intensity):
#     rend.glLine(V2(int(width - x * width/(2*intensity)), int(height/2)), V2(int(width/2), int(height/2 - x * height/(2*intensity))))

# Triángulo rectángulo
rend.glLine(V2(int(1.5 * width/12), int(height/2)), V2(int(2.5 * width/12), int(height/3)))
rend.glLine(V2(int(2.5 * width/12), int(height/3)), V2(int(2.5 * width/12), int(height/2)))
rend.glLine(V2(int(2.5 * width/12), int(height/2)), V2(int(1.5 * width/12), int(height/2)))

# Retángulo
rend.glLine(V2(int(3.25 * width/12), int(height/3)), V2(int(4.25 * width/12), int(height/3)))
rend.glLine(V2(int(3.25 * width/12), int(height/2)), V2(int(4.25 * width/12), int(height/2)))
rend.glLine(V2(int(3.25 * width/12), int(height/3)), V2(int(3.25 * width/12), int(height/2)))
rend.glLine(V2(int(4.25 * width/12), int(height/3)), V2(int(4.25 * width/12), int(height/2)))

# Triángulo Isósceles
rend.glLine(V2(int(5 * width/12), int(height/3)), V2(int(7 * width/12), int(height/3)))
rend.glLine(V2(int(5 * width/12), int(height/3)), V2(int(6 * width/12), int(2 * height/3)))
rend.glLine(V2(int(7 * width/12), int(height/3)), V2(int(6 * width/12), int(2 * height/3)))

# Trapezoide
rend.glLine(V2(int(8 * width/12), int(height/2)), V2(int(8.5 * width/12), int(height/2)))
rend.glLine(V2(int(7.5 * width/12), int(height/3)), V2(int(9 * width/12), int(height/3)))
rend.glLine(V2(int(7.5 * width/12), int(height/3)), V2(int(8 * width/12), int(height/2)))
rend.glLine(V2(int(9 * width/12), int(height/3)), V2(int(8.5 * width/12), int(height/2)))

# Triángulo rectángulo invertido
rend.glLine(V2(int(9.5 * width/12), int(height/3)), V2(int(10.5 * width/12), int(height/2)))
rend.glLine(V2(int(9.5 * width/12), int(height/3)), V2(int(9.5 * width/12), int(height/2)))
rend.glLine(V2(int(9.5 * width/12), int(height/2)), V2(int(10.5 * width/12), int(height/2)))

rend.glFinish("output.bmp")