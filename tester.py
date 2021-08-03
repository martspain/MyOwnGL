# Programa principal
from gl import Renderer, V2, color
import random

#Se establece el ancho y la altura de la imagen
width = 900
height = 450

polyOne = [V2(165, 380), V2(185, 360), V2(180, 330), V2(207, 345), V2(233, 330), V2(230, 360), V2(250, 380), V2(220, 385), V2(205, 410), V2(193, 383)]

polyTwo = [V2(321, 335), V2(288, 286), V2(339, 251), V2(374, 302)]

polyThree = [V2(377, 249), V2(411, 197), V2(436, 249)]

polyFour = [V2(413, 177), V2(448, 159), V2(502, 88), V2(553, 53), V2(535, 36), V2(676, 37), V2(660, 52),
V2(750, 145), V2(761, 179), V2(672, 192), V2(659, 214), V2(615, 214), V2(632, 230), V2(580, 230),
V2(597, 215), V2(552, 214), V2(517, 144), V2(466, 180)]

polyFive = [V2(682, 175), V2(708, 120), V2(735, 148), V2(739, 170)]


#Se crea la instancia
rend = Renderer(width, height)

rend.glClearColor(0,0,0)
rend.glColor(1,1,1)
rend.glClear()

#rend.glTriangle(V2(10, 10), V2(int(width/2), 400), V2(890, 10))

# rend.glPoint(165, 380)
# rend.glPoint(185, 360)
# rend.glPoint(180, 330)
# rend.glPoint(207, 345)
# rend.glPoint(165, 380)
# rend.glPoint(165, 380)
# rend.glPoint(165, 380)
# rend.glPoint(165, 380)

rend.glSolidPoly(polyOne, color(1,0,0))
rend.glSolidPoly(polyTwo, color(0,1,0))
rend.glSolidPoly(polyThree, color(0,0,1))
rend.glSolidPoly(polyFour, color(1,0,0))
rend.glSolidPoly(polyFive, color(0,0,0))

#rend.glPolyTest(polyOne, color(1,0,0))

# for i in rend.glLinePoints(V2(165, 380), V2(185, 360)):
#     rend.glPoint(i.x, i.y)
# for i in rend.glLinePoints(V2(185, 360), V2(180, 330)):
#     rend.glPoint(i.x, i.y)
# for i in rend.glLinePoints(V2(180, 330), V2(207, 345)):
#     rend.glPoint(i.x, i.y)
# for i in rend.glLinePoints(V2(207, 345), V2(233, 330)):
#     rend.glPoint(i.x, i.y)
# for i in rend.glLinePoints(V2(233, 330), V2(230, 360)):
#     rend.glPoint(i.x, i.y)
# for i in rend.glLinePoints(V2(230, 360), V2(250, 380)):
#     rend.glPoint(i.x, i.y)
# for i in rend.glLinePoints(V2(250, 380), V2(220, 385)):
#     rend.glPoint(i.x, i.y)
# for i in rend.glLinePoints(V2(220, 385), V2(205, 410)):
#     rend.glPoint(i.x, i.y)
# for i in rend.glLinePoints(V2(205, 410), V2(193, 383)):
#     rend.glPoint(i.x, i.y)
# for i in rend.glLinePoints(V2(193, 383), V2(165, 380)):
#     rend.glPoint(i.x, i.y)

#rend.glGetColor(V2(682, 175))

#rend.glLoadModel("statue.obj", V2(width/2, 0), V2(5.3, 5.3))
# Diseño alterno
#rend.glLoadModel("statue.obj", V2(1.5 * width/5, 0), V2(5.3, 5.3))
#rend.glLoadModel("statue.obj", V2(3.5 * width/5, 0), V2(5.3, 5.3), True)

rend.glFinish("output.bmp")